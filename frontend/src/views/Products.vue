<template>
  <div class="min-h-screen pb-20">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3">
        <h1 class="text-lg font-bold text-gray-800 text-center">宠物用品</h1>
      </div>
    </header>

    <div class="p-4">
      <!-- 加载状态 -->
      <div v-if="loading" class="flex justify-center py-12">
        <i class="fas fa-spinner fa-spin text-3xl text-primary"></i>
      </div>

      <!-- 商品列表 -->
      <div v-else class="grid grid-cols-2 gap-4">
        <div
          v-for="product in products"
          :key="product.id"
          class="bg-white rounded-2xl overflow-hidden shadow-md card-hover cursor-pointer"
          @click="goToDetail(product.id)"
        >
          <div class="relative overflow-hidden">
            <img :src="product.image" :alt="product.name" class="w-full h-40 object-cover gallery-img">
            <span v-if="product.hot" class="absolute top-2 right-2 bg-accent text-white text-xs px-2 py-1 rounded-full">
              <i class="fas fa-fire mr-1"></i>热门
            </span>
          </div>
          <div class="p-3">
            <h3 class="font-bold text-gray-800 text-sm mb-1">{{ product.name }}</h3>
            <p class="text-gray-500 text-xs mb-2 line-clamp-2">{{ product.description }}</p>
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
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'

const router = useRouter()
const appStore = useAppStore()

const loading = computed(() => appStore.loading)
const products = computed(() => appStore.products)

const goToDetail = (id) => {
  router.push(`/product/${id}`)
}

const addToCart = (product) => {
  appStore.addToCart(product)
}

onMounted(async () => {
  try {
    await appStore.fetchProducts()
  } catch (error) {
    console.error('Failed to load products:', error)
  }
})
</script>
