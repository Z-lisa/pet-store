from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class OrderItemBase(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    image: Optional[str] = None
    spec: Optional[str] = None


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    status: str = "pending"
    total_price: float
    shipping_price: float = 0
    discount: float = 0
    address: Optional[dict] = None
    shipping_method: Optional[str] = None
    remark: Optional[str] = None


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    total_price: float
    shipping_price: float = 0
    discount: float = 0
    address: Optional[dict] = None
    shipping_method: Optional[str] = None
    remark: Optional[str] = None


class OrderUpdate(BaseModel):
    status: Optional[str] = None


class OrderResponse(OrderBase):
    id: int
    created_at: Optional[datetime] = None
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
