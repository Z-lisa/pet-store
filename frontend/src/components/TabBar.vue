<template>
  <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-50 max-w-3xl mx-auto safe-area-pb">
    <div class="flex justify-around items-center h-16">
      <button
        v-for="item in tabs"
        :key="item.path"
        @click="handleTabClick(item)"
        class="flex flex-col items-center justify-center flex-1 h-full relative select-none"
        :class="{ 'text-accent': isActive(item.path), 'text-gray-500': !isActive(item.path) }"
      >
        <div class="relative transition-transform duration-200" :class="{ 'scale-110': isActive(item.path) }">
          <i :class="[item.icon, 'text-xl mb-1 block']"></i>
          <!-- 角标 -->
          <span
            v-if="item.badge && item.badge.value > 0"
            class="absolute -top-1 -right-2 min-w-[18px] h-[18px] bg-accent text-white text-xs rounded-full flex items-center justify-center px-1 font-medium"
          >
            {{ item.badge.max && item.badge.value > item.badge.max ? item.badge.max + '+' : item.badge.value }}
          </span>
          <!-- 小红点 -->
          <span
            v-else-if="item.dot"
            class="absolute -top-1 -right-1 w-2 h-2 bg-accent rounded-full"
          ></span>
        </div>
        <span class="text-xs font-medium">{{ item.name }}</span>
      </button>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'

const route = useRoute()
const router = useRouter()
const appStore = useAppStore()

// 购物车数量
const cartCount = computed(() => appStore.totalItems)

// 订单通知数量
const orderNotificationCount = computed(() => {
  return appStore.orders.filter(o => o.status === 'pending').length
})

// 导航配置
const tabs = [
  {
    name: '首页',
    path: '/',
    icon: 'fas fa-home'
  },
  {
    name: '服务',
    path: '/services',
    icon: 'fas fa-concierge-bell'
  },
  {
    name: '商品',
    path: '/products',
    icon: 'fas fa-shopping-bag'
  },
  {
    name: '购物车',
    path: '/cart',
    icon: 'fas fa-shopping-cart',
    badge: {
      value: cartCount,
      max: 99
    }
  },
  {
    name: '我的',
    path: '/profile',
    icon: 'fas fa-user',
    badge: {
      value: orderNotificationCount,
      max: 9
    }
  }
]

// 判断当前标签是否活跃
const isActive = (path) => {
  if (path === '/') {
    return route.path === '/'
  }
  return route.path === path || route.path.startsWith(path + '/')
}

// 处理标签点击
const handleTabClick = (item) => {
  if (route.path === item.path) {
    // 如果已经在当前页面，可以触发刷新或其他操作
    return
  }
  router.push(item.path)
}
</script>

<style scoped>
.safe-area-pb {
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
</style>
