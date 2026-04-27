from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingUpdate


def get_bookings(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None
) -> List[Booking]:
    query = db.query(Booking)
    if status:
        query = query.filter(Booking.status == status)
    return query.order_by(Booking.created_at.desc()).offset(skip).limit(limit).all()


def get_booking(db: Session, booking_id: int) -> Optional[Booking]:
    return db.query(Booking).filter(Booking.id == booking_id).first()


def create_booking(db: Session, booking: BookingCreate) -> Booking:
    db_booking = Booking(**booking.model_dump())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def update_booking(db: Session, booking_id: int, booking: BookingUpdate) -> Optional[Booking]:
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        return None
    
    if booking.status:
        db_booking.status = booking.status
    
    db.commit()
    db.refresh(db_booking)
    return db_booking


def delete_booking(db: Session, booking_id: int) -> bool:
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        return False
    
    db.delete(db_booking)
    db.commit()
    return True
