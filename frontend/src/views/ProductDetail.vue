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
            v-if="appStore.totalItems > 0"
            class="absolute -top-2 -right-2 w-5 h-5 bg-accent text-white text-xs rounded-full flex items-center justify-center"
          >
            {{ appStore.totalItems }}
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
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'

const route = useRoute()
const router = useRouter()
const appStore = useAppStore()

const quantity = ref(1)
const selectedSpec = ref('标准装')
const showSuccess = ref(false)

const specs = ['体验装', '标准装', '家庭装', '超值装']

const product = computed(() => {
  return appStore.products.find(p => p.id === parseInt(route.params.id))
})

const addToCart = () => {
  if (product.value) {
    for (let i = 0; i < quantity.value; i++) {
      appStore.addToCart({
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

onMounted(async () => {
  if (appStore.products.length === 0) {
    try {
      await appStore.fetchProducts()
    } catch (error) {
      console.error('Failed to load products:', error)
    }
  }
})
</script>
