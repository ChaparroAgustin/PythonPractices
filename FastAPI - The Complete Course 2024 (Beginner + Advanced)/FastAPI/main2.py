from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id, title, author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6) #gt= grater than and lt= lower than 

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'Coding on python',
                'description': 'A new description',
                'rating': 3
            }
        }


BOOKS = [
    Book(1, "Computer Science Pro ", "Coding", "A very nice book!", 5),
    Book(2, "Be Fast with FastAPI ", "Coding", "A great book!", 5),
    Book(3, "Master Endpoints", "Coding", "A awesome book!", 5),
    Book(4, "HP1", "Author 1", "Book Description", 5),
    Book(5, "HP2", "Author 2", "Book Description", 5),
    Book(6, "HP3", "Author 3", "Book Description", 5),
]

@app.get("/books")
async def readAllBooks():
    return BOOKS

@app.post("/create_book")
async def createBook(bookRequest: BookRequest):
    newBook = Book(**bookRequest.model_dump())
    BOOKS.append(findeBookId(newBook))
    return newBook

def findeBookId(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    
    return book

















