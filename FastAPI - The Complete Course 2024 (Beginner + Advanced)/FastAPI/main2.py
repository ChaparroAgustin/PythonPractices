from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date as dt

app = FastAPI()


class Book:
    id
    title: str
    author: str
    description: str
    rating: int
    publishDate: int

    def __init__(self,id, title, author,description,rating,publishDate):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publishDate = publishDate

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6) #gt= grater than and lt= lower than 
    publishDate: int = Field(lt = dt.today().year + 1)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'Coding on python',
                'description': 'A new description',
                'rating': 3,
                'pubish_date': 2012
            }
        }


BOOKS = [
    Book(1, "Computer Science Pro ", "Coding", "A very nice book!", 5, 2020),
    Book(2, "Be Fast with FastAPI ", "Coding", "A great book!", 4, 2015),
    Book(3, "Master Endpoints", "Coding", "A awesome book!", 2, 2003),
    Book(4, "HP1", "Author 1", "Book Description", 3, 2017),
    Book(5, "HP2", "Author 2", "Book Description", 1, 2019),
    Book(6, "HP3", "Author 3", "Book Description", 5, 2011),
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


@app.get("/book/{id}")
async def bookById(id: int):
    for book in BOOKS:
        if book.id == id:
            return book
    else:
        return {"book not found"}


@app.get("/books/")
async def booksByRating(bookRating: int):
    if (bookRating < 0 or bookRating > 5):
        return{"rating must be lower than 6 and higher than 0 "}
    booksToReturn = []
    for book in BOOKS:
        if book.rating == bookRating:
            booksToReturn.append(book)
    
    return booksToReturn

@app.put("/books/update_book")
async def updateBook(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            return book
    else:
        return {"book not found"}

@app.delete("/books/{id}")
async def deleteBook(bookId : int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == bookId:
            BOOKS.pop(i)
            return BOOKS[i]
        
    return {"Book not found"}



@app.get("/books/{date}")
async def booksBypublish(date: int):
    booksToReturn = []
    for book in BOOKS:
        if book.publishDate == date:
            booksToReturn.append(book)

    return booksToReturn
