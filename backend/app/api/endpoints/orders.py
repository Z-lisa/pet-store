from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.services import order_service

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=List[OrderResponse])
def list_orders(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """获取订单列表，支持状态筛选"""
    return order_service.get_orders(db, skip=skip, limit=limit, status=status)


@router.get("/statistics")
def get_statistics(db: Session = Depends(get_db)):
    """获取订单统计信息"""
    return order_service.get_order_statistics(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    """获取订单详情"""
    order = order_service.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="订单不存在")
    return order


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """创建订单"""
    return order_service.create_order(db, order)


@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    """更新订单状态"""
    updated = order_service.update_order(db, order_id, order)
    if not updated:
        raise HTTPException(status_code=404, detail="订单不存在")
    return updated


@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    """删除订单"""
    success = order_service.delete_order(db, order_id)
    if not success:
        raise HTTPException(status_code=404, detail="订单不存在")
    return {"message": "订单已删除"}
