from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class Product(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    rating: Optional[float] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    stock: Optional[int] = None