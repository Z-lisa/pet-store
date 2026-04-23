<template>
  <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-50 max-w-3xl mx-auto">
    <div class="flex justify-around items-center h-16">
      <router-link
        v-for="item in tabs"
        :key="item.path"
        :to="item.path"
        class="flex flex-col items-center justify-center flex-1 h-full relative"
        :class="{ 'text-accent': isActive(item.path), 'text-gray-500': !isActive(item.path) }"
      >
        <div class="relative">
          <i :class="item.icon" class="text-xl mb-1"></i>
          <!-- 购物车角标 -->
          <span
            v-if="item.path === '/cart' && cartStore.totalItems > 0"
            class="absolute -top-1 -right-2 min-w-[18px] h-[18px] bg-accent text-white text-xs rounded-full flex items-center justify-center px-1"
          >
            {{ cartStore.totalItems > 99 ? '99+' : cartStore.totalItems }}
          </span>
        </div>
        <span class="text-xs">{{ item.name }}</span>
      </router-link>
    </div>
  </nav>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const cartStore = useCartStore()

const tabs = [
  { name: '首页', path: '/', icon: 'fas fa-home' },
  { name: '服务', path: '/services', icon: 'fas fa-concierge-bell' },
  { name: '商品', path: '/products', icon: 'fas fa-shopping-bag' },
  { name: '购物车', path: '/cart', icon: 'fas fa-shopping-cart' },
  { name: '我的', path: '/orders', icon: 'fas fa-user' }
]

const isActive = (path) => {
  if (path === '/') {
    return route.path === '/'
  }
  return route.path.startsWith(path)
}
</script>
