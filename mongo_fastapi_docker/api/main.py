from fastapi import FastAPI
from src.routers import ROUTER

api = FastAPI()
api.include_router(router=ROUTER)