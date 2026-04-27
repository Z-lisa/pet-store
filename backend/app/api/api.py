from fastapi import APIRouter
from app.api.endpoints import products, services, orders, bookings

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(products.router)
api_router.include_router(services.router)
api_router.include_router(orders.router)
api_router.include_router(bookings.router)
