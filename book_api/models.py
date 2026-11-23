from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    reserved_by = Column(String, nullable=True)
    request_key = Column(String, nullable=True)