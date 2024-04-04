from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    telephone: str
    address: str
