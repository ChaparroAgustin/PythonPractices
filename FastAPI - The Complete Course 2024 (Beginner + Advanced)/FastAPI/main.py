from fastapi import FastAPI 



app = FastAPI()

# BOOKS = [
#     {'title':'title one','author':'Author one','category':'science'},
#     {'title':'title two','author':'Author two','category':'science'},
#     {'title':'title three','author':'Author three','category':'history'},
#     {'title':'title four','author':'Author four','category':'math'},
#     {'title':'title five','author':'Author five','category':'math'},
#     {'title':'title six','author':'Author six','category':'math'}
# ]

# file = open("BOOKS.txt", "w")
# for book in BOOKS:
#     libro = str(book)
#     file.writelines(libro + "\n")
# file.close()

BOOKS = []
file = open("BOOKS.txt","r+")
BOOKS = file.readlines()
print(BOOKS)
@app.get("/")
async def firstApi():
    return{"message":"Hello Agustin!!!"}


@app.get("/books")
async def showBooks():
    return BOOKS

@app.get("/books/{title}")
async def bookByTitle(title:str):
    bookToReturn = []
    for book in BOOKS:
        if(book.get('title').casefold() == title.casefold()):
            bookToReturn.append(book)
    return bookToReturn


@app.get("/books/")
async def bookByCategory_query(category: str):
    bookToReturn = []
    for book in BOOKS:
        if(book.get('category').casefold() == category.casefold()):
            bookToReturn.append(book)
    return bookToReturn
