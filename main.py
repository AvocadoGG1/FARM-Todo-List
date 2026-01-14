from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    is_offer: Union[bool, None] = None
    price: float
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
# Get request
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} 
# Put request
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id} 