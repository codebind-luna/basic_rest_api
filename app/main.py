from database import DbConn
import config
import falcon
import falconjsonio.middleware
from api import NoteCollectionResource, NoteResource


db_conn_obj  = DbConn(config.DATABASE_URL)
db_conn_obj.create_db_engine()
db_conn_obj.init_session()
db_session = db_conn_obj.db_session


app = falcon.API(
    middleware=[
        falconjsonio.middleware.RequireJSON(),
        falconjsonio.middleware.JSONTranslator(),
    ],
)

app.add_route('/notes', NoteCollectionResource(db_conn_obj.engine))
app.add_route('/notes/{id}', NoteResource(db_conn_obj.engine))
