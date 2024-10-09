from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# User Model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

# Post Model
class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

# Comment Model
class Comment(BaseModel):
    id: int
    content: str
    post_id: int
    author_id: int

# Sample  api

@app.get("/users", response_model=List[User])
def getusers():
    return ("users list")

@app.post("/users", response_model=List[User])
def getusers():
    return ("created users")

@app.put("/users", response_model=List[User])
def getusers():
    return ("updated users")

@app.get("/comments", response_model=List[User])
def getusers():
    return ("comments list")


@app.post("/comments", response_model=List[User])
def getusers():
    return ("comments updated")

@app.get("/photo", response_model=List[User])
def getusers():
    return ("photo got")

@app.put("/update/password", response_model=List[User])
def getusers():
    return ("password updated")