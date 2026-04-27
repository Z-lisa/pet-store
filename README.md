# 温馨宠物店 - 全栈项目 (Vue 3 + FastAPI)

## 项目简介
这是一个基于 Vue 3 + FastAPI 的全栈项目，包含宠物服务预约和宠物用品购买功能。前端采用 Vue 3 + Pinia 实现移动端 H5 商城，后端采用 Python FastAPI 提供 RESTful API 接口。

## 技术栈

### 前端
- **Vue 3** - 渐进式 JavaScript 框架（Composition API）
- **Vue Router 4** - 官方路由管理
- **Pinia** - 状态管理库
- **Vite 5** - 下一代前端构建工具
- **Tailwind CSS 3** - 原子化 CSS 框架
- **Font Awesome 6** - 图标库

### 后端
- **Python 3.13** - 编程语言
- **FastAPI** - 高性能 Web 框架
- **SQLAlchemy** - ORM 框架
- **SQLite** - 数据库
- **Uvicorn** - ASGI 服务器
- **Pydantic** - 数据验证

## 项目结构
```
pet-store/
├── backend/                    # 后端代码 (Python FastAPI)
│   ├── app/
│   │   ├── api/               # API 路由
│   │   │   └── endpoints/     # 各模块接口
│   │   ├── core/              # 核心配置
│   │   ├── db/                # 数据库配置
│   │   ├── models/            # 数据模型
│   │   ├── schemas/           # Pydantic 数据验证
│   │   ├── services/          # 业务逻辑
│   │   └── main.py            # FastAPI 应用入口
│   ├── requirements.txt       # Python 依赖
│   └── run.py                 # 启动脚本
├── frontend/                   # 前端代码 (Vue.js)
│   ├── src/
│   │   ├── assets/            # 静态资源
│   │   ├── components/        # 公共组件
│   │   ├── router/            # 路由配置
│   │   ├── services/          # API 服务层
│   │   ├── stores/            # Pinia 状态管理
│   │   └── views/             # 页面组件
│   ├── index.html             # 入口 HTML
│   ├── package.json           # 项目依赖配置
│   └── vite.config.js         # Vite 配置文件
└── start.bat                   # 项目启动脚本
```

## 核心功能

### 1. 首页 (Home.vue)
- Banner 轮播展示
- 快捷入口导航
- 热门商品推荐（后端 API 获取）
- 热门服务推荐（后端 API 获取）
- 店铺公告

### 2. 服务预约
- **服务列表** - 展示 4 类核心服务（后端 API 获取）
- **在线预约** - 表单提交预约信息（调用后端 API）
- 支持选择宠物类型、服务项目、预约时间

### 3. 商城购物
- **商品列表** - 分类筛选、搜索功能（后端 API 获取）
- **商品详情** - 规格选择、数量调整（后端 API 获取）
- **购物车** - 添加、删除、修改数量（本地存储）
- **订单确认** - 地址选择、配送方式、优惠计算（调用后端 API）

### 4. 订单管理
- **订单列表** - 状态筛选（全部/待付款/待发货/待收货）（后端 API 获取）
- **订单详情** - 查看订单完整信息（后端 API 获取）
- **订单状态** - 待付款/待发货/待收货/已完成/已取消

### 5. 底部导航
- 首页、服务、商品、购物车、我的
- 购物车角标实时显示数量

## API 接口

### 商品接口
- `GET /api/v1/products/` - 获取商品列表
- `GET /api/v1/products/{id}` - 获取商品详情
- `GET /api/v1/products/categories` - 获取商品分类

### 服务接口
- `GET /api/v1/services/` - 获取服务列表
- `GET /api/v1/services/{id}` - 获取服务详情

### 订单接口
- `GET /api/v1/orders/` - 获取订单列表
- `GET /api/v1/orders/{id}` - 获取订单详情
- `POST /api/v1/orders/` - 创建订单
- `PUT /api/v1/orders/{id}` - 更新订单
- `GET /api/v1/orders/statistics` - 获取订单统计

### 预约接口
- `GET /api/v1/bookings/` - 获取预约列表
- `POST /api/v1/bookings/` - 创建预约

## 页面路由

| 路由 | 页面 | 说明 |
|------|------|------|
| `/` | 首页 | 快捷入口、推荐商品 |
| `/about` | 关于我们 | 店铺介绍、环境展示 |
| `/services` | 服务项目 | 服务列表和预约入口 |
| `/products` | 商品列表 | 分类筛选、搜索 |
| `/product/:id` | 商品详情 | 规格选择、加入购物车 |
| `/cart` | 购物车 | 商品管理、去结算 |
| `/checkout` | 确认订单 | 地址、配送、支付 |
| `/orders` | 订单列表 | 订单状态管理 |
| `/order/:id` | 订单详情 | 订单完整信息 |
| `/contact` | 联系我们 | 联系方式、地图 |
| `/booking` | 在线预约 | 服务预约表单 |
| `/profile` | 个人中心 | 用户信息、订单统计 |

## 安装和运行

### 前端

#### 1. 安装依赖
```bash
cd frontend
npm install
```

#### 2. 运行开发服务器
```bash
npm run dev
```
访问 http://localhost:5173 预览项目

#### 3. 构建生产版本
```bash
npm run build
```

### 后端

#### 1. 创建虚拟环境
```bash
cd backend
python -m venv venv
```

#### 2. 激活虚拟环境
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

#### 3. 安装依赖
```bash
pip install -r requirements.txt
```

#### 4. 运行后端服务器
```bash
python run.py
```
访问 http://localhost:8000/docs 查看 API 文档

## 状态管理 (Pinia)

### App Store
```javascript
// 状态
products        // 商品列表（后端 API）
services        // 服务列表（后端 API）
orders          // 订单列表（后端 API）
bookings        // 预约列表（后端 API）
cartItems       // 购物车商品（本地存储）

// 计算属性
hotProducts     // 热门商品
totalItems      // 商品总数
totalPrice      // 商品总价
isEmpty         // 购物车是否为空

// 方法
fetchProducts() // 获取商品列表
fetchServices() // 获取服务列表
addToCart()     // 添加商品到购物车
removeFromCart()// 移除商品
updateQuantity()// 更新数量
clearCart()     // 清空购物车
createOrder()   // 创建订单
cancelOrder()   // 取消订单
createBooking() // 创建预约
```

## 交互功能

### 购物车功能
- ✅ 商品添加/删除
- ✅ 数量增减控制
- ✅ 实时价格计算
- ✅ 角标数量提示
- ✅ 本地存储持久化

### 订单流程
- ✅ 选择配送方式
- ✅ 地址信息管理
- ✅ 优惠券计算
- ✅ 订单状态跟踪
- ✅ 后端 API 交互

### 预约功能
- ✅ 宠物类型选择
- ✅ 服务项目选择
- ✅ 时间预约
- ✅ 表单验证
- ✅ 后端 API 交互

## 设计亮点

### 色彩搭配
- **主色调**: 暖黄色 (#FFD93D)
- **辅助色**: 浅蓝色 (#6BCBFF)
- **强调色**: 粉红色 (#FF8B94)

### 动画效果
- Vue 页面过渡动画
- 卡片悬停效果
- 添加购物车提示
- 模态框淡入淡出

### 移动端适配
- 底部固定导航栏
- 触摸友好的按钮尺寸
- 底部安全区域适配
- 页面切换过渡动画

### 前后端分离
- RESTful API 设计
- CORS 跨域配置
- 统一错误处理
- 加载状态管理

## 开发规范

### 前端
- 使用 Vue 3 Composition API (`<script setup>`)
- 组件命名使用 PascalCase
- 路由配置集中管理
- 状态管理使用 Pinia
- 样式使用 Tailwind CSS

### 后端
- 遵循 RESTful API 设计规范
- 使用 Pydantic 进行数据验证
- 业务逻辑与路由分离
- 统一错误响应格式

## 许可证
MIT License - 可自由使用和修改
