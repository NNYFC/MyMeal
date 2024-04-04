from fastapi import FastAPI

from src.model.user import User

application = FastAPI()


@application.get("/")
def root():
    return {"message": "Welcome to MyMEAL api!"}


@application.post("/register")
def registration(user: User):
    return user
