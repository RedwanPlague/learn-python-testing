from fastapi import FastAPI, HTTPException

from .schemas import Data

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Hello World!"}


@app.get("/list")
def get_list(start: int = 0, length: int = 5):
    return {"list": list(range(start, start + length))}


@app.post("/")
def use_data(data: Data):
    if data.id <= 0:
        raise HTTPException(400, "ID must be positive")
    return {"user": f"{data.name}_{data.id}"}
