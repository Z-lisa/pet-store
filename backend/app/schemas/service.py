from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: str
    duration: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    highlights: Optional[str] = None


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    duration: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    highlights: Optional[str] = None


class ServiceResponse(ServiceBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
