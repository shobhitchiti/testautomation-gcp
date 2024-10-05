import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Post model
class Post(BaseModel):
    title: str
    content: str
    published: bool

# Endpoint to create a new post
@app.post('/posts')
def create_post(post: Post):
    print(post.title)
    print(post.content)
    return {"message": "Post created successfully."}


@app.get('/posts')
def get_post():
    return {"message": "Post fetched successfully."}

@app.on_event("startup")
def save_openapi_schema():
    openapi_schema = app.openapi()
    with open("openapi_schema.json", "w") as f:
        json.dump(openapi_schema, f)