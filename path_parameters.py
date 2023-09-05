from enum import Enum

from fastapi import FastAPI, Query
# from pydantic import BaseModel
#
# from typing import Optional

app = FastAPI()



# path parameters...


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def post():
    return {"message": "hello from post route "}


@app.put("/")
async def put():
    return {"message": "hello from put route"}


@app.get("/users")
async def list_users():
    return {"message": "list users route"}

@app.get("/users/me")
async def get_current_user():
    return {"Message":"this is current user ID"}



@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = ("vegetables")
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name":food_name,"message":"you are healthy"}

    if food_name.value == 'fruits':
        return {
            "food_name":food_name,
            "message":"you are still healthy, but like sweet thins "
        }
    return {"food_name":food_name,"message":"I like chocolate milk"}
