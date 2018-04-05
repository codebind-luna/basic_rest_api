from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import config
from app.model import Base

class DbConn():
    def __init__(self, uri):
        self.uri = uri

    def create_db_engine(self):
        self.engine = create_engine(self.uri)

    def init_session(self):
        session = sessionmaker()
        session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.session = session
