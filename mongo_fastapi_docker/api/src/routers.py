from typing import List
from fastapi import (
    APIRouter,
    Depends,
    status,
    # HTTPException
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .models import (
    UserModel, 
    # UserListModel
)

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
    # await DB["users"].update_one(
    #     {"_id": new_user.inserted_id}
    # )
    created_user = await DB["users"].find_one(
        {"_id": new_user.inserted_id}
    )
    res = JSONResponse(
        status_code=status.HTTP_201_CREATED, 
        content=created_user
    )
    return res


# @ROUTER.post(
#     "/users/",
#     response_description="Add new user",
#     response_model=UserModel,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_user(user: UserModel):
# async def create_user(user: UserModel = Body(...)):

    # new_user= await users.insert_one(
    #         user.model_dump(by_alias=True, exclude=["id"])
    #     )
    # created_user = await users.find_one({"_id": new_user.inserted_id})

    # return created_user

# @api.get(
#     "/users/",
#     response_description="List all users",
#     response_model=UserListModel,
#     response_model_by_alias=False,
# )
# async def list_users():
#     """
#     List all of the student data in the database.

#     The response is unpaginated and limited to 1000 results.
#     """
#     return UserListModel(users=await users.find().to_list(1000))