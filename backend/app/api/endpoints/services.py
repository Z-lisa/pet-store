from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse
from app.services import service_service

router = APIRouter(prefix="/services", tags=["services"])


@router.get("/", response_model=List[ServiceResponse])
def list_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """获取服务列表"""
    return service_service.get_services(db, skip=skip, limit=limit)


@router.get("/{service_id}", response_model=ServiceResponse)
def get_service(service_id: int, db: Session = Depends(get_db)):
    """获取服务详情"""
    service = service_service.get_service(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="服务不存在")
    return service


@router.post("/", response_model=ServiceResponse)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    """创建服务（管理员）"""
    return service_service.create_service(db, service)


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(service_id: int, service: ServiceUpdate, db: Session = Depends(get_db)):
    """更新服务（管理员）"""
    updated = service_service.update_service(db, service_id, service)
    if not updated:
        raise HTTPException(status_code=404, detail="服务不存在")
    return updated


@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    """删除服务（管理员）"""
    success = service_service.delete_service(db, service_id)
    if not success:
        raise HTTPException(status_code=404, detail="服务不存在")
    return {"message": "服务已删除"}
