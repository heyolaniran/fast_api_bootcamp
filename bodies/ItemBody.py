from pydantic import BaseModel
class ItemBody(BaseModel): 
    id: int
    icon: str 
    title : str