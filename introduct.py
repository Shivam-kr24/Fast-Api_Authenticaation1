# from enum import Enum

from fastapi import FastAPI
# from pydantic import BaseModel

# from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Hello World"}



@app.post("/")
async def post():
    return {"message":"hello from post route "}


@app.put("/")
async def put():
    return {"message":"hello from put route"}


















