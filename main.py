from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

# Decorator allows this to hit the root 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Testing a new get method 
user_name = "Hello world"
@app.get("/return_user")
async def return_user_name():
    return user_name

@app.post("/createpost")
def create_posts(post: Post):
    print(post)
    return {}

# Will give title and content, both strings 