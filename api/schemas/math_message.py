from pydantic import BaseModel


class MathMessage(BaseModel):
    message: str
