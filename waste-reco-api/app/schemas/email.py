from pydantic import BaseModel, EmailStr
from typing import List, Optional

class DepositoItem(BaseModel):
    categoria: str
    cantidad: int

class EmailSchema(BaseModel):
    subject: str
    body: str
    to: EmailStr
    start_date: str
    end_date: str
    depositos: Optional[List[DepositoItem]] = None