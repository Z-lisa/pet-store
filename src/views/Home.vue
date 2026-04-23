<template>
  <div class="min-h-screen pb-20">
    <!-- 首页 Banner -->
    <section class="relative h-64 bg-gradient-to-r from-primary/20 to-secondary/20 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 opacity-30">
        <img src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=800" class="w-full h-full object-cover" alt="">
      </div>
      <div class="relative z-10 text-center px-4">
        <i class="fas fa-paw text-6xl text-accent mb-4 paw-print"></i>
        <h1 class="text-3xl font-bold text-gray-800 mb-2">温馨宠物店</h1>
        <p class="text-gray-600 mb-6">用爱呵护每一个小生命</p>
        <div class="flex gap-3 justify-center">
          <router-link to="/services" class="btn-primary px-6 py-3 rounded-full text-white font-bold shadow-lg">
            预约服务
          </router-link>
          <router-link to="/products" class="bg-white px-6 py-3 rounded-full text-gray-700 font-bold shadow-lg hover:bg-gray-50">
            浏览商品
          </router-link>
        </div>
      </div>
    </section>

    <!-- 快捷入口 -->
    <section class="py-6 px-4">
      <div class="grid grid-cols-4 gap-4">
        <router-link 
          v-for="item in quickLinks" 
          :key="item.path"
          :to="item.path"
          class="flex flex-col items-center p-4 bg-white rounded-2xl shadow-md card-hover"
        >
          <div class="w-12 h-12 rounded-full flex items-center justify-center text-white text-xl mb-2" :class="item.color">
            <i :class="item.icon"></i>
          </div>
          <span class="text-sm text-gray-700 font-medium">{{ item.name }}</span>
        </router-link>
      </div>
    </section>

    <!-- 推荐商品 -->
    <section class="py-4 px-4">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-lg font-bold text-gray-800">热门商品</h2>
        <router-link to="/products" class="text-secondary text-sm flex items-center">
          更多 <i class="fas fa-chevron-right ml-1"></i>
        </router-link>
      </div>
      <div class="grid grid-cols-2 gap-4">
        <div
          v-for="product in hotProducts"
          :key="product.id"
          class="bg-white rounded-2xl overflow-hidden shadow-md card-hover cursor-pointer"
          @click="goToProduct(product.id)"
        >
          <div class="relative overflow-hidden">
            <img :src="product.image" :alt="product.name" class="w-full h-32 object-cover gallery-img">
            <span v-if="product.hot" class="absolute top-2 right-2 bg-accent text-white text-xs px-2 py-1 rounded-full">
              <i class="fas fa-fire mr-1"></i>热门
            </span>
          </div>
          <div class="p-3">
            <h3 class="font-bold text-gray-800 text-sm mb-1 truncate">{{ product.name }}</h3>
            <div class="flex items-center justify-between">
              <span class="text-accent font-bold">¥{{ product.price }}</span>
              <button 
                @click.stop="addToCart(product)"
                class="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-all"
              >
                <i class="fas fa-plus text-xs"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 服务推荐 -->
    <section class="py-4 px-4">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-lg font-bold text-gray-800">热门服务</h2>
        <router-link to="/services" class="text-secondary text-sm flex items-center">
          更多 <i class="fas fa-chevron-right ml-1"></i>
        </router-link>
      </div>
      <div class="space-y-3">
        <router-link
          v-for="service in hotServices"
          :key="service.id"
          to="/services"
          class="flex items-center bg-white rounded-2xl p-4 shadow-md card-hover"
        >
          <div class="w-16 h-16 rounded-full flex items-center justify-center text-white text-2xl mr-4 flex-shrink-0" :class="service.color">
            <i :class="service.icon"></i>
          </div>
          <div class="flex-1 min-w-0">
            <h3 class="font-bold text-gray-800">{{ service.name }}</h3>
            <p class="text-gray-500 text-sm truncate">{{ service.description }}</p>
          </div>
          <i class="fas fa-chevron-right text-gray-400"></i>
        </router-link>
      </div>
    </section>

    <!-- 店铺公告 -->
    <section class="py-4 px-4">
      <div class="bg-gradient-to-r from-warm to-soft rounded-2xl p-4">
        <div class="flex items-center mb-2">
          <i class="fas fa-bullhorn text-accent mr-2"></i>
          <span class="font-bold text-gray-800">店铺公告</span>
        </div>
        <p class="text-gray-600 text-sm">新用户首单立减 20 元！注册会员享受更多优惠，快来体验我们的专业服务吧~</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cartStore = useCartStore()

const quickLinks = [
  { name: '服务项目', path: '/services', icon: 'fas fa-concierge-bell', color: 'bg-blue-500' },
  { name: '宠物用品', path: '/products', icon: 'fas fa-shopping-bag', color: 'bg-green-500' },
  { name: '在线预约', path: '/booking', icon: 'fas fa-calendar-check', color: 'bg-purple-500' },
  { name: '我的订单', path: '/orders', icon: 'fas fa-clipboard-list', color: 'bg-orange-500' }
]

const products = [
  {
    id: 1,
    name: '天然狗粮',
    description: '进口天然食材，无谷物配方，富含蛋白质',
    price: 168,
    category: 'food',
    image: 'https://images.unsplash.com/photo-1589924691195-41432c84c161?w=300',
    hot: true
  },
  {
    id: 2,
    name: '猫罐头套装',
    description: '多种口味组合，营养丰富，适口性佳',
    price: 89,
    category: 'food',
    image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300',
    hot: true
  },
  {
    id: 4,
    name: '互动球玩具',
    description: '智能滚动，自动避障，增加运动量',
    price: 128,
    category: 'toy',
    image: 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=300',
    hot: true
  },
  {
    id: 6,
    name: '保暖宠物窝',
    description: '加厚保暖，防风防水，冬季必备',
    price: 228,
    category: 'bed',
    image: 'https://images.unsplash.com/photo-1597843786271-105124152c92?w=300',
    hot: true
  }
]

const hotProducts = computed(() => products.filter(p => p.hot))

const hotServices = [
  {
    id: 1,
    name: '宠物洗护',
    description: '专业洗护流程，使用天然无害洗护产品',
    icon: 'fas fa-shower',
    color: 'bg-gradient-to-br from-blue-400 to-blue-600'
  },
  {
    id: 2,
    name: '美容造型',
    description: '资深美容师设计专属造型，打造萌宠形象',
    icon: 'fas fa-cut',
    color: 'bg-gradient-to-br from-pink-400 to-pink-600'
  }
]

const goToProduct = (id) => {
  router.push(`/product/${id}`)
}

const addToCart = (product) => {
  cartStore.addToCart(product)
}
</script>
