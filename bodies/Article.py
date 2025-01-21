from pydantic import BaseModel, Field

class Article(BaseModel):
    name: str
    description: str | None = Field(None, description="Description for the article", title="Description", max_length=25)
    price: float = Field(... , gt=0, description="Article price > 0")
    tax : float | None = None
