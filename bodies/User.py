from pydantic import BaseModel

class User(BaseModel): 
    username: str 
    email: str 
    password : str
    birthday : str | None = None 
    status : bool = True