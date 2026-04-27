from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.api.api import api_router
from app.db.database import engine, Base
from app.services import product_service, service_service
from app.schemas.product import ProductCreate
from app.schemas.service import ServiceCreate
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "欢迎使用温馨宠物店 API",
        "docs": "/docs",
        "version": settings.VERSION
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


def init_db_data():
    """Initialize database with sample data"""
    db = SessionLocal()
    try:
        # Check if products exist
        existing_products = product_service.get_products(db, limit=1)
        if not existing_products:
            # Add sample products
            sample_products = [
                ProductCreate(
                    name="天然狗粮",
                    description="进口天然食材，无谷物配方，富含蛋白质",
                    price=168,
                    category="food",
                    image="https://images.unsplash.com/photo-1589924691195-41432c84c161?w=300",
                    hot=True
                ),
                ProductCreate(
                    name="猫罐头套装",
                    description="多种口味组合，营养丰富，适口性佳",
                    price=89,
                    category="food",
                    image="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300",
                    hot=True
                ),
                ProductCreate(
                    name="宠物咬胶",
                    description="耐咬磨牙，清洁牙齿，安全无毒",
                    price=35,
                    category="toy",
                    image="https://images.unsplash.com/photo-1576201836106-db1758fd1497?w=300"
                ),
                ProductCreate(
                    name="互动球玩具",
                    description="智能滚动，自动避障，增加运动量",
                    price=128,
                    category="toy",
                    image="https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=300",
                    hot=True
                ),
                ProductCreate(
                    name="宠物窝垫",
                    description="柔软舒适，可拆洗，四季通用",
                    price=158,
                    category="bed",
                    image="https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=300"
                ),
                ProductCreate(
                    name="保暖宠物窝",
                    description="加厚保暖，防风防水，冬季必备",
                    price=228,
                    category="bed",
                    image="https://images.unsplash.com/photo-1597843786271-105124152c92?w=300",
                    hot=True
                ),
                ProductCreate(
                    name="宠物毛衣",
                    description="纯棉材质，保暖透气，多色可选",
                    price=78,
                    category="clothes",
                    image="https://images.unsplash.com/photo-1560743641-3914f2c45636?w=300"
                ),
                ProductCreate(
                    name="宠物雨衣",
                    description="防水透气，反光条设计，安全出行",
                    price=98,
                    category="clothes",
                    image="https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=300"
                )
            ]
            for product in sample_products:
                product_service.create_product(db, product)
        
        # Check if services exist
        existing_services = service_service.get_services(db, limit=1)
        if not existing_services:
            # Add sample services
            sample_services = [
                ServiceCreate(
                    name="宠物洗护",
                    description="专业洗护流程，使用天然无害洗护产品，深层清洁毛发，去除异味，让爱宠焕然一新。包含：基础洗浴、护毛护理、指甲修剪、耳道清洁等全套服务。",
                    price="¥68 起",
                    duration="60-90 分钟",
                    icon="fas fa-shower",
                    color="bg-gradient-to-br from-blue-400 to-blue-600",
                    highlights="药浴护理,皮肤检查,耳道清洁,指甲修剪"
                ),
                ServiceCreate(
                    name="美容造型",
                    description="资深美容师根据宠物品种特点和个人喜好，设计专属造型，修剪毛发，打造萌宠形象。使用专业美容工具，确保安全舒适。",
                    price="¥128 起",
                    duration="90-120 分钟",
                    icon="fas fa-cut",
                    color="bg-gradient-to-br from-pink-400 to-pink-600",
                    highlights="精修造型,染色设计,SPA 护理,精油按摩"
                ),
                ServiceCreate(
                    name="寄养看护",
                    description="宽敞舒适的寄养环境，24 小时监控，定时遛弯互动，让爱宠在主人外出期间也能享受家的温暖。每日提供活动视频反馈。",
                    price="¥88/天",
                    duration="按天计费",
                    icon="fas fa-home",
                    color="bg-gradient-to-br from-green-400 to-green-600",
                    highlights="独立空间,定时喂食,互动陪伴,健康观察"
                ),
                ServiceCreate(
                    name="疫苗保健",
                    description="提供全套疫苗接种服务，定期健康检查，驱虫防疫，建立健康档案，守护宠物健康。所有疫苗均为正规渠道进口产品。",
                    price="¥168 起",
                    duration="30-60 分钟",
                    icon="fas fa-syringe",
                    color="bg-gradient-to-br from-purple-400 to-purple-600",
                    highlights="进口疫苗,体检套餐,驱虫服务,健康咨询"
                )
            ]
            for service in sample_services:
                service_service.create_service(db, service)
    finally:
        db.close()


# Initialize data on startup
init_db_data()
