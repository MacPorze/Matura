from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer,primary_key=True)
    province = Column(String, nullable=False)
    passed = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)

def read_db(query,*params):
    session = create_session()
    for year in session.query(query,params):
        print(year)

    session.close()
    return


def write_db(db_data):
    session = create_session()

    session.add_all(db_data)
    session.commit()

    session.close()


def create_session():
    engine = create_engine("sqlite:///exams.db")
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def create_db():
    engine = create_engine('sqlite:///exams.db')
    Base.metadata.create_all(engine)