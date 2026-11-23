from sqlalchemy.orm import Session
from models import Book
from database import engine

def Creat_book(title):
    with Session(engine) as db:
        book = Book(title = title)
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

def reserve_book(book_id, reader, request_key):
    with Session(engine) as db:
        book = (db.scalar(Book).filter(book.id == book_id).with_for_update())

        if not book:
            raise ValueError("book not found")
        
            