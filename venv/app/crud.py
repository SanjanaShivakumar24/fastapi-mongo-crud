# crud.py
from app.database import collection

async def create_user(user_data: dict):
    result = await collection.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id)
    return user_data

async def get_users():
    users = []
    async for user in collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

async def get_user_by_name(name: str):
    user = await collection.find_one({"name": name})
    if user:
        user["_id"] = str(user["_id"])
    return user

async def update_user(name: str, data: dict):
    await collection.update_one({"name": name}, {"$set": data})
    return await get_user_by_name(name)


async def delete_user(name: str):
    result = await collection.delete_one({"name": name})
    return {"deleted": result.deleted_count}
