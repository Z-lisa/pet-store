from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services import product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[ProductResponse])
def list_products(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    search: Optional[str] = None,
    hot_only: bool = False,
    db: Session = Depends(get_db)
):
    """获取商品列表，支持分类筛选、搜索和热门筛选"""
    return product_service.get_products(
        db, skip=skip, limit=limit, category=category, search=search, hot_only=hot_only
    )


@router.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    """获取所有商品分类"""
    from sqlalchemy import distinct
    categories = db.query(distinct(product_service.Product.category)).all()
    return [{"id": cat[0], "name": _get_category_name(cat[0])} for cat in categories]


def _get_category_name(category_id: str) -> str:
    """获取分类中文名称"""
    names = {
        "food": "食品",
        "toy": "玩具",
        "bed": "窝垫",
        "clothes": "服饰"
    }
    return names.get(category_id, category_id)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """获取商品详情"""
    product = product_service.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="商品不存在")
    return product


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """创建商品（管理员）"""
    return product_service.create_product(db, product)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """更新商品（管理员）"""
    updated = product_service.update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="商品不存在")
    return updated


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """删除商品（管理员）"""
    success = product_service.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="商品不存在")
    return {"message": "商品已删除"}
