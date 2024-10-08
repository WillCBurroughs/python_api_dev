from fastapi import FastAPI, Response, status, HTTPException
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
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
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/default")
def add_random_post():
    post = {"title": "This is a default post", "content": "Here you can see ...", "id": randrange(0, 100000)}
    post_dict = post.model_dump()
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with {id} does not exist")
    post_dict = post.model_dump()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data" : post_dict}

