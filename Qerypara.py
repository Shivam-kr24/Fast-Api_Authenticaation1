from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel

# from typing import Optional

app = FastAPI()




# ------>> Query Parameters &String Validation <<<------------

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
    return {"Message": "this is current user ID"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == 'fruits':
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet thins "
        }
    return {"food_name": food_name, "message": "I like chocolate milk"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        # return {"item_id":item_id, "q":q}
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit amet, consecrate disciplining elit. Crash biennium."
            }

        )
        return item
    # return {"item_id":item_id}


@app.get("/users/{user_id} / items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False
                        ):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "Lorem ipsum dolor sit amet, consecrate disciplining elit. Crash biennium."

             }
        )
    return item


class Item(BaseModel):
    name: str
    description: str | None = None
    price: int
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items")
# async def read_items(q: list[str] = Query(["foo","bar"])):
async def read_items(
        q:str
        | None = Query(
            None,
            max_length=10,
            min_length=3,
            title= "sample query string",
            description= "this is a sample query string",
            alias="item-query"
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_hidden/hidden")
async def hidden_query_route(hidden_query:str|None = Query(None,include_in_schema=False)):
    if hidden_query:
        return {"hidden_query":hidden_query}
    return {"hidden_query": "Not Found"}
