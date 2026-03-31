from fastapi import APIRouter
from pydantic import BaseModel
from services import item_service


router = APIRouter()

class ItemCreate(BaseModel):
    item_name: str
    category: str
    price: float
    stock_quantity: int

@router.get("/api/items")
def get_items():
    return item_service.fetch_items_from_db()

@router.get("/api/items/{item_id}")
def get_single_item(item_id: int):
    return item_service.fetch_single_item_from_db(item_id)

@router.post("/api/items")
def create_item(item_data: ItemCreate):
    return item_service.add_item_to_db(item_data)