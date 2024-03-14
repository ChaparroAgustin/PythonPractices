from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()


class book:
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
    id: int
    title: str 
    authos: str
    description: str
    rating: int


BOOKS = [
    book(1, "Computer Science Pro ", "Coding", "A very nice book!", 5),
    book(1, "Be Fast with FastAPI ", "Coding", "A great book!", 5),
    book(1, "Master Endpoints", "Coding", "A awesome book!", 5),
    book(1, "HP1", "Author 1", "Book Description", 5),
    book(1, "HP2", "Author 2", "Book Description", 5),
    book(1, "HP3", "Author 3", "Book Description", 5),
]

@app.get("/books")
async def readAllBooks():
    return BOOKS

@app.post("/create_book")
async def createBook(bookRequest: BookRequest):
    BOOKS.append(bookRequest)



















