from sqlalchemy import Column, Integer, String, Boolean, DATE, ForeignKey
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()


class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    calories = Column(Integer,default=0)
    fat = Column(Integer,default=0)
    carbo = Column(Integer,default=0)
    protein = Column(Integer,default=0)
    compound = Column(Boolean,default=False)
    
class History(Base):
    __tablename__ = 'history'
    
    id = Column(Integer, primary_key=True)
    calories = Column(Integer,default=0)
    date = Column(DATE)
    
class HistoryEntry(Base):
    __tablename__ = "historyentry"
    
    id = Column(Integer, primary_key=True)
    foodId = Column(Integer, ForeignKey("foods.id"))