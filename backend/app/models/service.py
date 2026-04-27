from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=True)
    price = Column(String(50), nullable=False)
    duration = Column(String(50), nullable=True)
    icon = Column(String(50), nullable=True)
    color = Column(String(100), nullable=True)
    highlights = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
