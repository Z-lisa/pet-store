# 项目结构说明

## 快速开始

### 方式一：使用批处理文件（推荐）
1. 双击 `install.bat` 安装依赖
2. 双击 `start.bat` 启动开发服务器

### 方式二：命令行
```bash
# 1. 打开命令行，进入项目目录
cd c:\Users\EDY\Desktop\shop

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run dev
```

## Vue 项目结构详解

```
shop/
├── 📄 index.html              # 入口 HTML 文件
│   └── 包含 Font Awesome 图标库和 Vue 挂载点
│
├── 📦 package.json            # 项目配置文件
│   ├── 项目名称、版本、描述
│   ├── 依赖：vue, vue-router
│   └── 开发依赖：vite, tailwindcss, @vitejs/plugin-vue
│
├── ⚙️ vite.config.js          # Vite 构建工具配置
│   ├── Vue 插件配置
│   ├── 路径别名：@ -> ./src
│   └── 开发服务器：端口 8080，自动打开浏览器
│
├── 🎨 tailwind.config.js      # Tailwind CSS 配置
│   └── 自定义颜色主题
│
├── 📝 postcss.config.js       # PostCSS 配置
│   └── 启用 Tailwind CSS 和 Autoprefixer
│
├── 📁 src/                    # 源代码目录
│   │
│   ├── 📄 main.js             # 应用入口文件
│   │   └── 创建 Vue 应用并挂载到 #app
│   │
│   ├── 📄 App.vue             # 根组件
│   │   ├── 导入所有子组件
│   │   ├── 滚动监听逻辑
│   │   └── 页面整体布局
│   │
│   ├── 📁 assets/             # 静态资源
│   │   └── main.css           # 全局样式文件
│   │       ├── Tailwind CSS 指令
│   │       ├── 自定义 CSS 样式
│   │       └── 动画效果定义
│   │
│   └── 📁 components/         # Vue 组件目录
│       ├── Header.vue         # 头部导航组件
│       │   ├── 响应式导航栏
│       │   ├── 移动端菜单
│       │   └── 滚动监听高亮
│       │
│       ├── About.vue          # 店铺介绍组件
│       │   ├── 店铺简介
│       │   ├── 经营理念/服务优势
│       │   └── 图片画廊
│       │
│       ├── Services.vue       # 服务项目组件
│       │   └── 4 项服务卡片展示
│       │
│       ├── Products.vue       # 宠物用品组件
│       │   ├── 分类筛选
│       │   └── 商品网格展示
│       │
│       ├── Contact.vue        # 联系方式组件
│       │   ├── 地址/电话/营业时间
│       │   └── 地图占位
│       │
│       ├── Booking.vue        # 在线预约组件
│       │   ├── 预约表单
│       │   ├── 表单验证
│       │   └── 成功提示
│       │
│       ├── Footer.vue         # 页脚组件
│       │   └── 社交媒体链接
│       │
│       └── BackToTop.vue      # 返回顶部组件
│           └── 滚动显示/隐藏
│
├── 📄 README.md               # 项目说明文档
├── 📄 .gitignore              # Git 忽略文件配置
├── 📄 install.bat             # 一键安装依赖脚本
└── 📄 start.bat               # 一键启动项目脚本
```

## 组件通信说明

### 父子组件通信
- **App.vue (父)** → **Header.vue (子)**
  - 使用 `v-model:activeSection` 双向绑定
  - 滚动监听自动更新导航状态

### 组件数据流
```
App.vue (根组件)
  ├── Header.vue - 导航（双向绑定 activeSection）
  ├── About.vue - 店铺介绍（独立数据）
  ├── Services.vue - 服务项目（独立数据）
  ├── Products.vue - 宠物用品（独立数据 + 计算属性）
  ├── Contact.vue - 联系方式（独立数据）
  ├── Booking.vue - 在线预约（表单验证 + 成功提示）
  ├── Footer.vue - 页脚（静态内容）
  └── BackToTop.vue - 返回顶部（滚动监听）
```

## 技术要点

### 1. Vue 3 Composition API
所有组件使用 `<script setup>` 语法糖，代码更简洁：
```vue
<script setup>
import { ref, computed } from 'vue'

// 响应式数据
const count = ref(0)

// 计算属性
const doubled = computed(() => count.value * 2)
</script>
```

### 2. Tailwind CSS 原子化样式
```vue
<template>
  <div class="flex items-center justify-center bg-primary text-white">
    内容
  </div>
</template>
```

### 3. Vue 过渡动画
```vue
<transition name="fade">
  <div v-show="visible">内容</div>
</transition>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
```

### 4. 响应式布局
使用 Tailwind 的响应式前缀：
- `md:` - 中等屏幕（≥768px）
- `lg:` - 大屏幕（≥1024px）

## 常用命令

```bash
# 开发模式
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

## 文件修改指南

### 修改店铺信息
编辑 `src/components/Contact.vue` 中的 `contactInfo` 对象

### 修改服务项目
编辑 `src/components/Services.vue` 中的 `services` 数组

### 修改商品数据
编辑 `src/components/Products.vue` 中的 `products` 数组

### 修改配色方案
编辑 `tailwind.config.js` 中的 `colors` 配置

### 添加新组件
1. 在 `src/components/` 目录创建新 `.vue` 文件
2. 在 `App.vue` 中导入并使用

## 部署说明

### 构建项目
```bash
npm run build
```
构建完成后，`dist` 目录包含所有静态文件

### 部署到服务器
将 `dist` 目录上传到任何静态网站托管服务：
- Vercel
- Netlify
- GitHub Pages
- 自有服务器

## 常见问题

### Q: 如何修改端口号？
A: 编辑 `vite.config.js`，修改 `server.port` 的值

### Q: 如何添加新页面？
A: 
1. 安装 vue-router: `npm install vue-router`
2. 创建 `src/router/index.js`
3. 配置路由
4. 在 `main.js` 中使用 router

### Q: 如何添加后端 API？
A: 在组件中使用 `fetch` 或 `axios` 调用 API：
```vue
<script setup>
import { ref, onMounted } from 'vue'

const data = ref([])

onMounted(async () => {
  const response = await fetch('API_URL')
  data.value = await response.json()
})
</script>
```
