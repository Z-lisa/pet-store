<template>
  <div class="min-h-screen bg-gray-50 pb-20">
    <!-- 用户信息卡片 -->
    <section class="bg-gradient-to-br from-primary to-secondary p-6 text-white">
      <div class="flex items-center gap-4">
        <div class="w-16 h-16 rounded-full bg-white/20 flex items-center justify-center text-3xl">
          <i class="fas fa-user"></i>
        </div>
        <div>
          <h2 class="text-xl font-bold">宠物主人</h2>
          <p class="text-white/80 text-sm">VIP 会员</p>
        </div>
      </div>
      <div class="flex justify-around mt-6">
        <div class="text-center">
          <div class="text-2xl font-bold">{{ orders.length }}</div>
          <div class="text-sm text-white/80">全部订单</div>
        </div>
        <div class="text-center">
          <div class="text-2xl font-bold">{{ pendingCount }}</div>
          <div class="text-sm text-white/80">待付款</div>
        </div>
        <div class="text-center">
          <div class="text-2xl font-bold">{{ couponCount }}</div>
          <div class="text-sm text-white/80">优惠券</div>
        </div>
      </div>
    </section>

    <!-- 订单状态 -->
    <section class="bg-white mx-4 -mt-4 rounded-2xl shadow-md p-4 relative z-10">
      <div class="flex justify-between items-center mb-4">
        <h3 class="font-bold text-gray-800">我的订单</h3>
        <router-link to="/orders" class="text-gray-500 text-sm flex items-center">
          查看全部 <i class="fas fa-chevron-right ml-1 text-xs"></i>
        </router-link>
      </div>
      <div class="flex justify-around">
        <router-link
          v-for="item in orderStatuses"
          :key="item.status"
          to="/orders"
          class="flex flex-col items-center gap-2 relative"
        >
          <div class="w-10 h-10 rounded-full bg-gray-50 flex items-center justify-center text-lg text-gray-600">
            <i :class="item.icon"></i>
          </div>
          <span class="text-xs text-gray-600">{{ item.label }}</span>
          <span
            v-if="item.count > 0"
            class="absolute -top-1 -right-1 w-4 h-4 bg-accent text-white text-xs rounded-full flex items-center justify-center"
          >
            {{ item.count }}
          </span>
        </router-link>
      </div>
    </section>

    <!-- 功能菜单 -->
    <section class="bg-white mx-4 mt-4 rounded-2xl shadow-md overflow-hidden">
      <div
        v-for="(menu, index) in menus"
        :key="menu.path"
        @click="handleMenuClick(menu)"
        class="flex items-center px-4 py-4 cursor-pointer hover:bg-gray-50 transition-colors"
        :class="{ 'border-t': index > 0 }"
      >
        <div class="w-8 h-8 rounded-lg flex items-center justify-center text-white mr-3" :class="menu.color">
          <i :class="menu.icon"></i>
        </div>
        <span class="flex-1 text-gray-800">{{ menu.label }}</span>
        <i class="fas fa-chevron-right text-gray-400 text-sm"></i>
      </div>
    </section>

    <!-- 客服电话 -->
    <section class="text-center py-6 text-gray-500 text-sm">
      <p>客服热线: 400-888-8888</p>
      <p class="mt-1">工作时间: 9:00 - 21:00</p>
    </section>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'

const router = useRouter()
const appStore = useAppStore()

const orders = computed(() => appStore.orders)
const couponCount = 3

const pendingCount = computed(() => {
  return orders.value.filter(o => o.status === 'pending').length
})

const orderStatuses = [
  { status: 'pending', label: '待付款', icon: 'fas fa-wallet', count: computed(() => orders.value.filter(o => o.status === 'pending').length) },
  { status: 'paid', label: '待服务', icon: 'fas fa-clock', count: 0 },
  { status: 'completed', label: '已完成', icon: 'fas fa-check-circle', count: computed(() => orders.value.filter(o => o.status === 'completed').length) },
  { status: 'cancelled', label: '已取消', icon: 'fas fa-times-circle', count: computed(() => orders.value.filter(o => o.status === 'cancelled').length) }
]

const menus = [
  { label: '收货地址', icon: 'fas fa-map-marker-alt', color: 'bg-blue-500', path: '/address' },
  { label: '我的预约', icon: 'fas fa-calendar-alt', color: 'bg-green-500', path: '/booking' },
  { label: '优惠券', icon: 'fas fa-ticket-alt', color: 'bg-red-500', path: '/coupons' },
  { label: '联系客服', icon: 'fas fa-headset', color: 'bg-purple-500', path: '/contact' },
  { label: '关于我们', icon: 'fas fa-info-circle', color: 'bg-gray-500', path: '/about' }
]

const handleMenuClick = (menu) => {
  if (menu.path === '/address' || menu.path === '/coupons') {
    alert('功能开发中...')
    return
  }
  router.push(menu.path)
}

onMounted(async () => {
  try {
    await appStore.fetchOrders()
  } catch (error) {
    console.error('Failed to load orders:', error)
  }
})
</script>
