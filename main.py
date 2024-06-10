from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()
from Pydentic import BaseModel
@app.post("/")
async def create_item():
    return {"message": "Hello from the post route"}

@app.put("/")
async def update_item():
    return {"message": "Hello from the put route"}

@app.get("/user")
async def get_current_user():
    return {"message": "Sefo is a great Man Of God"}

@app.get("/fruit")
async def get_current_fruit():
    return {"message": "Sefo is a great pastor"}

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetable = "vegetable"
    dairy = "dairy"

@app.get("/food/{foodenum}")
async def get_food(foodenum: FoodEnum):
    if foodenum == FoodEnum.vegetable:
        return {"foodname": foodenum, "message": "You are healthy"}
    elif foodenum == FoodEnum.dairy:
        return {"foodname": foodenum, "message": "You are a child"}
    elif foodenum == FoodEnum.fruits:
        return {"foodname": foodenum, "message": "Backend API is secured"}

class SportEnum(str, Enum):
    chest = "chestpress"
    leg = "squat"
    shoulder = "pullup"

@app.get("/sport/{sport}")
async def get_sport(sport: SportEnum):
    if sport == SportEnum.chest:
        return {"message": "Your chest is big, bro! Keep working."}
    elif sport == SportEnum.leg:
        return {"message": "Big leg!"}
    elif sport == SportEnum.shoulder:
        return {"message": "Big shoulder, bro! Keep going."}
fake_item_db=[{"item_name":"foo"},{"item_name":"bar"},{"item_name":"box"}]
@app.get("/item")
async def list_item(skip: int=0,limit: int =10):
    return fake_item_db[skip:skip+limit]
@app.get("/item/{item_id}")
async def get_item(item_id:str,query:Optional[str]=None,short:bool=False):
    item={"item_id":item_id}
    if short:
        item.update({"query":query})
        return item
    else:
        return {"item_id":item_id,"query":"this is the long query of the becuase the short is False"}

class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price :float
    tax:Optional[float]=None
@app.post("/item")
async def item_post(item:Item):
    return item
