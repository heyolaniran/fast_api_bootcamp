from fastapi import FastAPI
from enum import Enum
from constants import items;
from Enums import ItemEnum
from typing import Optional
app =  FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Hello World"}

@app.get("/users")
async def users(): 
    return { "message" : "Users lists" }

@app.get("/users/me")
async def current_user(): 
    return { "message": "current user " }

@app.get("/users/{id}")
async def user(id : int):
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


@app.get("/items")
async def items_list(skip: int = 0 , limit: int = 10): 
    return items[skip : skip+limit]


@app.get("/items/{item_id}")
async def items_detail(item_id: int , q : Optional[ItemEnum] = None): # q is optional => q :  str | None = None

    list = {"item": items[item_id]}; 
    if q : 
        list.update({ q : items[item_id][q] })
    
    return list

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_items(user_id: int , item_id : int, q : str | None = None): 
    result = { "user": user_id }
    list  = await items_detail(item_id, q); 
    result.update(list)

    return result

