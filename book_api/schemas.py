from pydantic import BaseModel, ConfigDict

class CreateBook(BaseModel):
    title:str

class BookReserve(BaseModel):
    book_id: int
    reader:str
    request_key:str

class BookResponse(BaseModel):
    id:int
    title:str
    reserved_by:str
    request_key:str

    model_config = ConfigDict(from_attributes = True)