from pydantic import BaseModel
from enum import Enum

class DogImage(BaseModel):
    image_bytes: bytes
    top_n: int = 3
