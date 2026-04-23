# 温馨宠物店 - Vue 3 移动端 H5 商城

## 项目简介
这是一个基于 Vue 3 的移动端 H5 商城项目，包含宠物服务预约和宠物用品购买功能。采用 Vue Router 实现多页面路由，Pinia 进行状态管理。

## 技术栈
- **Vue 3** - 渐进式 JavaScript 框架（Composition API）
- **Vue Router 4** - 官方路由管理
- **Pinia** - 状态管理库
- **Vite 5** - 下一代前端构建工具
- **Tailwind CSS 3** - 原子化 CSS 框架
- **Font Awesome 6** - 图标库

## 项目结构
```
shop/
├── index.html              # 入口 HTML
├── package.json            # 项目依赖配置
├── vite.config.js          # Vite 配置文件
├── tailwind.config.js      # Tailwind CSS 配置
├── postcss.config.js       # PostCSS 配置
├── README.md               # 项目说明文档
├── src/
│   ├── main.js             # 应用入口文件
│   ├── App.vue             # 根组件
│   ├── router/             # 路由配置
│   │   └── index.js        # 路由定义
│   ├── stores/             # Pinia 状态管理
│   │   └── cart.js         # 购物车状态
│   ├── components/         # 公共组件
│   │   └── TabBar.vue      # 底部导航栏
│   ├── views/              # 页面组件
│   │   ├── Home.vue        # 首页
│   │   ├── About.vue       # 关于我们
│   │   ├── Services.vue    # 服务项目
│   │   ├── Products.vue    # 商品列表
│   │   ├── ProductDetail.vue # 商品详情
│   │   ├── Cart.vue        # 购物车
│   │   ├── Checkout.vue    # 订单确认
│   │   ├── Orders.vue      # 订单列表
│   │   ├── OrderDetail.vue # 订单详情
│   │   ├── Contact.vue     # 联系我们
│   │   └── Booking.vue     # 在线预约
│   └── assets/
│       └── main.css        # 全局样式
```

## 核心功能

### 1. 首页 (Home.vue)
- Banner 轮播展示
- 快捷入口导航
- 热门商品推荐
- 热门服务推荐
- 店铺公告

### 2. 服务预约
- **服务列表** - 展示 4 类核心服务
- **在线预约** - 表单提交预约信息
- 支持选择宠物类型、服务项目、预约时间

### 3. 商城购物
- **商品列表** - 分类筛选、搜索功能
- **商品详情** - 规格选择、数量调整
- **购物车** - 添加、删除、修改数量
- **订单确认** - 地址选择、配送方式、优惠计算

### 4. 订单管理
- **订单列表** - 状态筛选（全部/待付款/待发货/待收货）
- **订单详情** - 查看订单完整信息
- **订单状态** - 待付款/待发货/待收货/已完成/已取消

### 5. 底部导航
- 首页、服务、商品、购物车、我的
- 购物车角标实时显示数量

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

## 安装和运行

### 1. 安装依赖
```bash
npm install
```

### 2. 运行开发服务器
```bash
npm run dev
```
访问 http://localhost:8080 预览项目

### 3. 构建生产版本
```bash
npm run build
```

## 状态管理 (Pinia)

### Cart Store
```javascript
// 状态
items           // 购物车商品列表
orders          // 订单列表

// 计算属性
totalItems      // 商品总数
totalPrice      // 商品总价
isEmpty         // 购物车是否为空

// 方法
addToCart()     // 添加商品
removeFromCart() // 移除商品
updateQuantity() // 更新数量
clearCart()     // 清空购物车
createOrder()   // 创建订单
cancelOrder()   // 取消订单
```

## 交互功能

### 购物车功能
- ✅ 商品添加/删除
- ✅ 数量增减控制
- ✅ 实时价格计算
- ✅ 角标数量提示

### 订单流程
- ✅ 选择配送方式
- ✅ 地址信息管理
- ✅ 优惠券计算
- ✅ 订单状态跟踪

### 预约功能
- ✅ 宠物类型选择
- ✅ 服务项目选择
- ✅ 时间预约
- ✅ 表单验证

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

## 开发规范

- 使用 Vue 3 Composition API (`<script setup>`)
- 组件命名使用 PascalCase
- 路由配置集中管理
- 状态管理使用 Pinia
- 样式使用 Tailwind CSS

## 后续优化建议

1. 添加真实的地图 API 集成
2. 接入后端 API 实现真实数据
3. 添加用户登录/注册功能
4. 集成微信支付/支付宝支付
5. 添加商品收藏功能
6. 实现真实的服务预约系统
7. 添加评价系统
8. 实现消息通知功能

## 许可证
MIT License - 可自由使用和修改
