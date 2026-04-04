from fastapi import APIRouter
from pydantic import BaseModel
from services import item_service

router = APIRouter(tags=["User Management"])

@router.get("/api/users")
def get_all_users():
   return "hello World"
