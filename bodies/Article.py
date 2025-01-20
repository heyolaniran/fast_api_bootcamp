from pydantic import BaseModel

class Article(BaseModel):
    name: str
    description: str | None = None 
    price: float
    tax : float | None = None
    