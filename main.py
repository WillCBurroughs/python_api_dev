from fastapi import FastAPI

app = FastAPI()

# Decorator allows this to hit the root 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Testing a new get method 
user_name = "Hello world"
@app.get("/return_user")
async def return_user_name():
    return user_name


