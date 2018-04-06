from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

class DbConn():
    def __init__(self, uri):
        self.uri = uri

    def create_db_engine(self):
        self.engine = create_engine(self.uri)

    def init_session(self):
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        session = Session()
        session._model_changes = {}
        Base.metadata.create_all(self.engine)
        self.db_session = session
