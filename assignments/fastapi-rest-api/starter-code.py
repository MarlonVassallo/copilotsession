# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example data model
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool = True

# Example in-memory storage
items = []

# TODO: Implement endpoints for CRUD operations

# Example GET endpoint
@app.get("/items")
def get_items():
    return items

# Example POST endpoint
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

# Add more endpoints for update, delete, and retrieve by ID
