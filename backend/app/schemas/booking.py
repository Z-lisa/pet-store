from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BookingBase(BaseModel):
    name: str
    phone: str
    pet_type: str
    pet_name: Optional[str] = None
    service: str
    date: str
    time: Optional[str] = None
    remark: Optional[str] = None


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BaseModel):
    status: Optional[str] = None


class BookingResponse(BookingBase):
    id: int
    status: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
