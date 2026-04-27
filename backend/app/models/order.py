from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(20), default="pending")
    total_price = Column(Float, nullable=False)
    shipping_price = Column(Float, default=0)
    discount = Column(Float, default=0)
    address = Column(JSON, nullable=True)
    shipping_method = Column(String(50), nullable=True)
    remark = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=1)
    image = Column(String(500), nullable=True)
    spec = Column(String(100), nullable=True)
    
    order = relationship("Order", back_populates="items")
