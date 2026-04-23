from fastapi import FastAPI
from src.main.routes.users_routes import users_router

app = FastAPI()

app.include_router(users_router)
