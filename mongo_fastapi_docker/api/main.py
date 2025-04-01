# import uvicorn
# from typing import Optional, List
# from typing_extensions import Annotated

# from pydantic import BaseModel, Field
# from pydantic.functional_validators import BeforeValidator
# from src.models import PyObjectId

# from fastapi import FastAPI, status, Body
from fastapi import FastAPI

# from src.settings import DB

from src.routers import ROUTER

api = FastAPI()
api.include_router(router=ROUTER)

# user = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'root')
# password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', 'example')
# uri = f'mongodb://{user}:{password}@mongodb:27017'
# print(uri)
# # client = MongoClient(uri)
# uri = "mongodb://localhost:27017/"
# client = AsyncIOMotorClient(uri)

# db = client["test-database"]
# users = db.get_collection("users")

# -- MODELS -- #
# PyObjectId = Annotated[str, BeforeValidator(str)]

# class UserModel(BaseModel):
#     id: Optional[PyObjectId] = Field(alias="_id", default=None)
#     name: str = Field(...)
#     email: str = Field(...)

# class UserCollection(BaseModel):
#     users: List[UserModel]

# @api.post(
#     "/users/",
#     response_description="Add new user",
#     response_model=UserModel,
#     status_code=status.HTTP_201_CREATED
# )
# async def create_user(user: UserModel = Body(...)):

#     new_user= await DB["users"].insert_one(
#             user.model_dump(by_alias=True, exclude=["id"])
#         )
#     created_user = await DB["users"].find_one({"_id": new_user.inserted_id})

#     # new_user = await DB["users"].insert_one(user)
#     # created_user = await DB["users"].find_one({"_id": new_user.inserted_id})

#     return created_user

# @api.get(
#     "/users/",
#     response_description="List all users",
#     response_model=UserCollection,
#     response_model_by_alias=False,
# )
# async def list_users():
#     """
#     List all of the student data in the database.

#     The response is unpaginated and limited to 1000 results.
#     """
#     # return UserListModel(users=await users.find().to_list(1000))
#     # users = await DB["users"].find().to_list(1000)
#     # return UserCollection(users=users)
#     return UserCollection(users = await DB["users"].find().to_list(1000))

# from src.routers import router
# api.include_router(router)


# if __name__ == "__main__":
#     uvicorn.run(
#         "main:api",
#         host="0.0.0.0",
#         port=8000, 
#         reload=True
#     )