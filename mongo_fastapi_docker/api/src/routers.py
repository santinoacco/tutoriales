from typing import List
from fastapi import (
    APIRouter,
    status,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .models import UserModel 

from .settings import DB

ROUTER = APIRouter()

@ROUTER.get(
    "/users",
    response_description="List all users",
    response_model=List[UserModel]
)
async def list_users():
    users = await DB["users"].find().to_list(1000)
    return users

@ROUTER.post(
    "/users/",
    response_description="Add new user",
    response_model=UserModel,
)
async def create_user(user: UserModel):
    # TODO: validate user doesn't already exist.
    user_json = jsonable_encoder(user)
    new_user = await DB["users"].insert_one(user_json)
    created_user = await DB["users"].find_one(
        {"_id": new_user.inserted_id}
    )
    res = JSONResponse(
        status_code=status.HTTP_201_CREATED, 
        content=created_user
    )
    return res