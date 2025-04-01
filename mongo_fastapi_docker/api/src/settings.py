import os
from motor.motor_asyncio import AsyncIOMotorClient


# CLIENT = AsyncIOMotorClient( "mongodb://localhost:27017/")
CLIENT = AsyncIOMotorClient(os.environ["DB_URL"])
# DB = CLIENT['testDB']
DB = CLIENT[os.environ["MONGO_INITDB_DATABASE"]]
