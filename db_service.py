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

class Service:
    def read_db(self, selector,*params):
        session = self.create_session()
        if selector == 1:
            if len(params) == 4:
                result = session.query(Data.value).filter(Data.province==params[0],Data.year>=params[1],
                                                          Data.year<=params[2],Data.gender==params[3],
                                                          Data.passed=="przystąpiło")
            elif len(params) == 3:
                result = session.query(Data.value).filter(Data.province == params[0], Data.year >= params[1],
                                                          Data.year <= params[2], Data.passed == "przystąpiło")

        if selector == 2:
            if len(params) == 3:
                passed = session.query(Data.value).filter(Data.province==params[0],Data.year==params[1],
                                                          Data.gender==params[2],Data.passed == "zdało")
                tooked = session.query(Data.value).filter(Data.province==params[0],Data.year==params[1],
                                                          Data.gender==params[2],Data.passed == "przystąpiło")
            elif len(params) == 2:
                passed = session.query(Data.value).filter(Data.province == params[0], Data.year == params[1],
                                                          Data.passed=="zdało")
                tooked = session.query(Data.value).filter(Data.province == params[0], Data.year == params[1],
                                                          Data.passed == "przystąpiło")
            result = (passed,tooked)
        session.close()
        return result


    def write_db(self,db_data):
        session = self.create_session()

        session.add_all(db_data)
        session.commit()

        session.close()

    def create_session(self):
        engine = create_engine("sqlite:///exams.db")
        Base.metadata.create_all(engine)

        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session

    def create_db(self):
        engine = create_engine('sqlite:///exams.db')
        Base.metadata.create_all(engine)