from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "Favorite foods", "content": "I like pizza", "id": 2}]

# Decorator allows this to hit the root 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Testing a new get method 
user_name = "Hello world"
@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[-1]
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = 404
    return {"post_detail": post}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        

# Will give title and content, both strings 