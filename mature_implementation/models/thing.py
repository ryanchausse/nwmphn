from sqlalchemy import Column, DateTime, Integer, String, Boolean, Float
from mature_implementation.db.base import Base

class Thing(Base):
    __tablename__ = "things"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    is_true = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
