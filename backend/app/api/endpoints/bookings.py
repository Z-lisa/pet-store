from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.schemas.booking import BookingCreate, BookingUpdate, BookingResponse
from app.services import booking_service

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.get("/", response_model=List[BookingResponse])
def list_bookings(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """获取预约列表"""
    return booking_service.get_bookings(db, skip=skip, limit=limit, status=status)


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    """获取预约详情"""
    booking = booking_service.get_booking(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="预约不存在")
    return booking


@router.post("/", response_model=BookingResponse)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    """创建预约"""
    return booking_service.create_booking(db, booking)


@router.put("/{booking_id}", response_model=BookingResponse)
def update_booking(booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)):
    """更新预约状态"""
    updated = booking_service.update_booking(db, booking_id, booking)
    if not updated:
        raise HTTPException(status_code=404, detail="预约不存在")
    return updated


@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    """删除预约"""
    success = booking_service.delete_booking(db, booking_id)
    if not success:
        raise HTTPException(status_code=404, detail="预约不存在")
    return {"message": "预约已删除"}
