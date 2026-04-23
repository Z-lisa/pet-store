<template>
  <div class="min-h-screen bg-gray-50 pb-24">
    <!-- 返回按钮 -->
    <div class="fixed top-4 left-4 z-50">
      <button 
        @click="$router.back()"
        class="w-10 h-10 rounded-full bg-white/90 backdrop-blur shadow-lg flex items-center justify-center"
      >
        <i class="fas fa-arrow-left text-gray-600"></i>
      </button>
    </div>

    <!-- 商品图片 -->
    <div class="relative h-72 bg-white">
      <img :src="product?.image" :alt="product?.name" class="w-full h-full object-cover">
      <div v-if="product?.hot" class="absolute top-4 right-4 bg-accent text-white px-3 py-1 rounded-full text-sm">
        <i class="fas fa-fire mr-1"></i>热门
      </div>
    </div>

    <!-- 商品信息 -->
    <div class="bg-white rounded-t-3xl -mt-6 relative z-10 px-4 py-6">
      <div class="flex justify-between items-start mb-2">
        <h1 class="text-xl font-bold text-gray-800 flex-1">{{ product?.name }}</h1>
        <span class="text-2xl font-bold text-accent ml-4">¥{{ product?.price }}</span>
      </div>
      <p class="text-gray-500 mb-4">{{ product?.description }}</p>

      <!-- 规格选择 -->
      <div class="mb-6">
        <h3 class="font-bold text-gray-800 mb-3">选择规格</h3>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="spec in specs"
            :key="spec"
            @click="selectedSpec = spec"
            class="px-4 py-2 rounded-full border-2 transition-all"
            :class="selectedSpec === spec 
              ? 'border-primary bg-primary/10 text-primary font-bold' 
              : 'border-gray-200 text-gray-600 hover:border-primary/50'"
          >
            {{ spec }}
          </button>
        </div>
      </div>

      <!-- 数量选择 -->
      <div class="mb-6">
        <h3 class="font-bold text-gray-800 mb-3">购买数量</h3>
        <div class="flex items-center">
          <button 
            @click="quantity > 1 && quantity--"
            class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-gray-600"
            :class="{ 'opacity-50': quantity <= 1 }"
          >
            <i class="fas fa-minus"></i>
          </button>
          <span class="w-16 text-center font-bold text-lg">{{ quantity }}</span>
          <button 
            @click="quantity++"
            class="w-10 h-10 rounded-full border-2 border-gray-200 flex items-center justify-center text-gray-600"
          >
            <i class="fas fa-plus"></i>
          </button>
        </div>
      </div>

      <!-- 商品详情 -->
      <div class="mb-6">
        <h3 class="font-bold text-gray-800 mb-3">商品详情</h3>
        <div class="text-gray-600 text-sm space-y-2">
          <p><i class="fas fa-check-circle text-primary mr-2"></i>100% 正品保证</p>
          <p><i class="fas fa-check-circle text-primary mr-2"></i>7天无理由退换</p>
          <p><i class="fas fa-check-circle text-primary mr-2"></i>满99元包邮</p>
          <p><i class="fas fa-check-circle text-primary mr-2"></i>24小时内发货</p>
        </div>
      </div>
    </div>

    <!-- 底部操作栏 -->
    <div class="fixed bottom-0 left-0 right-0 bg-white border-t px-4 py-3 flex items-center gap-3 max-w-3xl mx-auto">
      <div class="flex gap-4 px-4">
        <router-link to="/cart" class="relative">
          <i class="fas fa-shopping-cart text-xl text-gray-600"></i>
          <span 
            v-if="cartStore.totalItems > 0"
            class="absolute -top-2 -right-2 w-5 h-5 bg-accent text-white text-xs rounded-full flex items-center justify-center"
          >
            {{ cartStore.totalItems }}
          </span>
        </router-link>
      </div>
      <button 
        @click="addToCart"
        class="flex-1 bg-primary text-white py-3 rounded-full font-bold shadow-lg hover:shadow-xl transition-shadow"
      >
        加入购物车
      </button>
      <button 
        @click="buyNow"
        class="flex-1 btn-primary text-white py-3 rounded-full font-bold shadow-lg"
      >
        立即购买
      </button>
    </div>

    <!-- 添加成功提示 -->
    <transition name="fade">
      <div v-if="showSuccess" class="fixed top-20 left-1/2 transform -translate-x-1/2 bg-green-500 text-white px-6 py-3 rounded-full shadow-lg z-50 flex items-center">
        <i class="fas fa-check-circle mr-2"></i>
        已添加到购物车
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cartStore = useCartStore()

const quantity = ref(1)
const selectedSpec = ref('标准装')
const showSuccess = ref(false)

const specs = ['体验装', '标准装', '家庭装', '超值装']

const products = [
  {
    id: 1,
    name: '天然狗粮',
    description: '进口天然食材，无谷物配方，富含蛋白质，适合各年龄段犬只',
    price: 168,
    category: 'food',
    image: 'https://images.unsplash.com/photo-1589924691195-41432c84c161?w=400',
    hot: true
  },
  {
    id: 2,
    name: '猫罐头套装',
    description: '多种口味组合，营养丰富，适口性佳，满足猫咪挑剔味蕾',
    price: 89,
    category: 'food',
    image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400',
    hot: true
  },
  {
    id: 3,
    name: '宠物咬胶',
    description: '耐咬磨牙，清洁牙齿，安全无毒，让宠物远离拆家',
    price: 35,
    category: 'toy',
    image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1497?w=400',
    hot: false
  },
  {
    id: 4,
    name: '互动球玩具',
    description: '智能滚动，自动避障，增加运动量，让宠物爱上运动',
    price: 128,
    category: 'toy',
    image: 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400',
    hot: true
  },
  {
    id: 5,
    name: '宠物窝垫',
    description: '柔软舒适，可拆洗，四季通用，给宠物一个温暖的家',
    price: 158,
    category: 'bed',
    image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400',
    hot: false
  },
  {
    id: 6,
    name: '保暖宠物窝',
    description: '加厚保暖，防风防水，冬季必备，让宠物温暖过冬',
    price: 228,
    category: 'bed',
    image: 'https://images.unsplash.com/photo-1597843786271-105124152c92?w=400',
    hot: true
  },
  {
    id: 7,
    name: '宠物毛衣',
    description: '纯棉材质，保暖透气，多色可选，时尚又实用',
    price: 78,
    category: 'clothes',
    image: 'https://images.unsplash.com/photo-1560743641-3914f2c45636?w=400',
    hot: false
  },
  {
    id: 8,
    name: '宠物雨衣',
    description: '防水透气，反光条设计，安全出行，雨天也能愉快散步',
    price: 98,
    category: 'clothes',
    image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=400',
    hot: false
  }
]

const product = computed(() => {
  return products.find(p => p.id === parseInt(route.params.id))
})

const addToCart = () => {
  if (product.value) {
    for (let i = 0; i < quantity.value; i++) {
      cartStore.addToCart({
        ...product.value,
        spec: selectedSpec.value
      })
    }
    showSuccess.value = true
    setTimeout(() => {
      showSuccess.value = false
    }, 2000)
  }
}

const buyNow = () => {
  addToCart()
  router.push('/checkout')
}
</script>
