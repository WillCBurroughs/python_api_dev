from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "Favorite foods", "content": "I like pizza", "id": 2}]

# Decorator allows this to hit the root 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Testing a new get method 
user_name = "Hello world"
@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/createpost")
def create_posts(post: Post):
    print(post)
    return {}

# Will give title and content, both strings 