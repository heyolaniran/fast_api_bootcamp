from fastapi import FastAPI
from enum import Enum
app =  FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Hello World"}

@app.get("/users")
async def items(): 
    return { "message" : "Users lists" }

@app.get("/users/me")
async def current_user(): 
    return { "message": "current user " }

@app.get("/users/{id}")
async def item(id : int):
    return {"message": f'user {id}'}

class FoodEum(str , Enum): 
    fruits = "fruits"
    vegetables ="vegetables"
    dairy = "dairy"

@app.get("/foods/{name}")

async def get_food(name: FoodEum):

    if name == FoodEum.vegetables: 
        return { "name": name ,  "message": "You are healthy " }
    elif name.value == "fruits" : 
        return { "message": f"You are eating {name.value} " } 
    else :
        return { "name": name , "message": " treat you well" }
