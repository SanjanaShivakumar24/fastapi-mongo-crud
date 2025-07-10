from fastapi import APIRouter
from app.models import User
from app import crud
 
router = APIRouter()
 
@router.get("/")
async def root():
    return {"message": "Welcome to the FastAPI + MongoDB CRUD app"}
 
@router.post("/user")
async def add_user(user: User):
    return await crud.create_user(user.dict())
 
@router.get("/users")
async def list_users():
    return await crud.get_users()
 
@router.get("/user/{name}")
async def get_user(name: str):
    return await crud.get_user_by_name(name)

@router.put("/user/{name}")
async def update_user(name: str, user: User):
    return await crud.update_user(name, user.dict())

 
@router.delete("/user/{name}")
async def delete_user(name: str):
    return await crud.delete_user(name)
