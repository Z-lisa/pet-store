from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate, OrderUpdate


def get_orders(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None
) -> List[Order]:
    query = db.query(Order)
    if status and status != "all":
        query = query.filter(Order.status == status)
    return query.order_by(Order.created_at.desc()).offset(skip).limit(limit).all()


def get_order(db: Session, order_id: int) -> Optional[Order]:
    return db.query(Order).filter(Order.id == order_id).first()


def create_order(db: Session, order: OrderCreate) -> Order:
    db_order = Order(
        status="pending",
        total_price=order.total_price,
        shipping_price=order.shipping_price,
        discount=order.discount,
        address=order.address,
        shipping_method=order.shipping_method,
        remark=order.remark
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    # Create order items
    for item in order.items:
        db_item = OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            name=item.name,
            price=item.price,
            quantity=item.quantity,
            image=item.image,
            spec=item.spec
        )
        db.add(db_item)
    
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id: int, order: OrderUpdate) -> Optional[Order]:
    db_order = get_order(db, order_id)
    if not db_order:
        return None
    
    if order.status:
        db_order.status = order.status
    
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int) -> bool:
    db_order = get_order(db, order_id)
    if not db_order:
        return False
    
    db.delete(db_order)
    db.commit()
    return True


def get_order_statistics(db: Session) -> dict:
    total = db.query(Order).count()
    pending = db.query(Order).filter(Order.status == "pending").count()
    paid = db.query(Order).filter(Order.status == "paid").count()
    shipped = db.query(Order).filter(Order.status == "shipped").count()
    completed = db.query(Order).filter(Order.status == "completed").count()
    cancelled = db.query(Order).filter(Order.status == "cancelled").count()
    
    return {
        "total": total,
        "pending": pending,
        "paid": paid,
        "shipped": shipped,
        "completed": completed,
        "cancelled": cancelled
    }
