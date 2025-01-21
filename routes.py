from main import app
from enum import Enum
from constants import items;
from Enums import ItemEnum
from typing import Optional
from bodies import ItemBody, Article, User
from fastapi import Query, Path, Body

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

# Body request 

@app.post("/items/create")
async def create_item(item: ItemBody): 
    items.append(item); 

    return items; 

@app.put("/items/{id}/update")
async def update_items(id: int , item : ItemBody, q: Optional[ItemEnum] = None):
    
    element = items[id]
    for (key, value) in item:
        element[key]=value
    if q : 
        return element[q]; 
    return element 

# Query Params and String validation 

@app.get("/validations")
async def query_validation(q: Optional[list[str]] = Query(["foo", "bar"], description="Fields to fetch", alias="field") ): 
    result = { "items": items }

    if q: 
        result.update({ "q" : q })
    
    return result

# Query params and numeric validation 

@app.get("/query_validations/{item_id}")
async def numeric_validation(item_id : int = Path(... , ge=0, lt=len(items)) , q :Optional[str] = Query(None)): 
    element = items[item_id]; 
    if q : 
        element.update({ "q" : q  })
    return element


# Part 7 : Multiple Params 

@app.put("/articles/{id}")
async def update_article(*, id: int = Path(..., ge=0, le=10), q: Optional[str] =  None , article : Article = Body(... , embed=True) ): 
    result = { "article id": id }

    if q : 
        result.update({ "q": q})
    
    if article : 
        result.update({ "article": article })
    return result ; 
# Part 8 :  Body fields

@app.put("/update_article/{article_id}") 
async def update_article_routes(article_id: int , article : Article = Body(...) ):
    result = { "id": article_id , "article": article}

    return result; 