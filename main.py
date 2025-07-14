from typing import Annotated

from fastapi import FastAPI, Pathdff
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello():
    return {
        "message": "hello index",
        }

@app.get("/hello/")
def hello(name: str = "world"):
    return {"message": f"hello {name.upper()}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {"message": "Success", 
            "email": user.email,        
        }


@app.post("/calc/add/")
def calc(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }
    

@app.get("/hihihaha/")
def items():
    return {
        "1": "1hah",
        "2": "2hah",
        "3": "3hah",
    }

@app.get("/hihihaha/latest/")
def get_latest_item():
    return {"id": "latest"}


@app.get("/hihihaha/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item": {
            "id": item_id,
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
