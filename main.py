from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
import uvicorn

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

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


@app.post("/calc/add/")
def calc(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
