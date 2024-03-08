# nicio del Server: uvicorn main:app --reload
# https://www.youtube.com/watch?v=_y9qQZXE24A

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    username: str
    age: int
    url: str


users_list = [
    User(id=1, name="Brais", username="Moure", url="https://google.com", age=35),
    User(id=2 ,name="Brais", username="Moure", url="https://google.com", age=35),
    User(id=3 ,name="Brais", username="Moure", url="https://google.com", age=35),
    User(id=4 ,name="Brais", username="Moure", url="https://google.com", age=35),
]


@app.get("/")
async def userJson():
    return {"message": "Hola mundo!"}


@app.get("/users")
async def users():
    return users_list


@app.get("/user/{id}")
async def userById(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return ({"error":f"User with id:{id} not found"})