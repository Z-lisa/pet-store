<template>
  <div class="min-h-screen bg-gray-50 pb-20">
    <!-- 头部 -->
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3">
        <h1 class="text-lg font-bold text-gray-800 text-center">我的订单</h1>
      </div>
      <!-- 订单状态筛选 -->
      <div class="flex border-b">
        <button
          v-for="tab in tabs"
          :key="tab.value"
          @click="activeTab = tab.value"
          class="flex-1 py-3 text-sm font-medium transition-colors relative"
          :class="activeTab === tab.value ? 'text-accent' : 'text-gray-500'"
        >
          {{ tab.label }}
          <span 
            v-if="tab.value !== 'all' && getCount(tab.value) > 0"
            class="absolute top-1 right-2 w-4 h-4 bg-accent text-white text-xs rounded-full flex items-center justify-center"
          >
            {{ getCount(tab.value) }}
          </span>
          <div 
            v-if="activeTab === tab.value"
            class="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-8 h-0.5 bg-accent"
          ></div>
        </button>
      </div>
    </header>

    <!-- 订单列表 -->
    <div class="p-4 space-y-4">
      <div
        v-for="order in filteredOrders"
        :key="order.id"
        class="bg-white rounded-2xl p-4 shadow-md"
        @click="goToOrderDetail(order.id)"
      >
        <!-- 订单头部 -->
        <div class="flex justify-between items-center mb-3 pb-3 border-b">
          <span class="text-gray-500 text-sm">订单号: {{ order.id }}</span>
          <span 
            class="text-sm font-medium"
            :class="getStatusColor(order.status)"
          >
            {{ getStatusText(order.status) }}
          </span>
        </div>

        <!-- 商品信息 -->
        <div class="space-y-3 mb-3">
          <div
            v-for="item in order.items.slice(0, 2)"
            :key="item.id"
            class="flex gap-3"
          >
            <img :src="item.image" :alt="item.name" class="w-16 h-16 object-cover rounded-lg">
            <div class="flex-1">
              <h3 class="font-medium text-gray-800 text-sm">{{ item.name }}</h3>
              <p class="text-gray-500 text-xs">x{{ item.quantity }}</p>
            </div>
            <span class="text-gray-800 font-medium">¥{{ item.price }}</span>
          </div>
          <p v-if="order.items.length > 2" class="text-gray-500 text-sm">
            共 {{ order.items.length }} 件商品
          </p>
        </div>

        <!-- 订单底部 -->
        <div class="flex justify-between items-center pt-3 border-t">
          <span class="text-gray-500 text-sm">
            {{ formatDate(order.createdAt) }}
          </span>
          <div class="flex items-center gap-2">
            <span class="text-gray-500 text-sm">实付:</span>
            <span class="text-accent font-bold">¥{{ order.totalPrice + order.shippingPrice - order.discount }}</span>
          </div>
        </div>

        <!-- 操作按钮 -->
        <div class="flex gap-2 mt-3 justify-end">
          <button 
            v-if="order.status === 'pending'"
            @click.stop="cancelOrder(order.id)"
            class="px-4 py-2 rounded-full border border-gray-300 text-gray-600 text-sm"
          >
            取消订单
          </button>
          <button 
            v-if="order.status === 'pending'"
            class="px-4 py-2 rounded-full bg-primary text-white text-sm font-medium"
          >
            去支付
          </button>
          <button 
            v-if="order.status === 'completed'"
            class="px-4 py-2 rounded-full border border-gray-300 text-gray-600 text-sm"
          >
            申请售后
          </button>
        </div>
      </div>

      <!-- 空状态 -->
      <div v-if="filteredOrders.length === 0" class="flex flex-col items-center justify-center py-20">
        <i class="fas fa-clipboard-list text-6xl text-gray-300 mb-4"></i>
        <p class="text-gray-500 mb-4">暂无订单</p>
        <router-link 
          to="/products" 
          class="btn-primary px-6 py-3 rounded-full text-white font-bold"
        >
          去购物
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cartStore = useCartStore()

const activeTab = ref('all')

const tabs = [
  { label: '全部', value: 'all' },
  { label: '待付款', value: 'pending' },
  { label: '待发货', value: 'paid' },
  { label: '待收货', value: 'shipped' }
]

const filteredOrders = computed(() => {
  if (activeTab.value === 'all') {
    return cartStore.orders
  }
  return cartStore.orders.filter(order => order.status === activeTab.value)
})

const getCount = (status) => {
  return cartStore.orders.filter(order => order.status === status).length
}

const getStatusText = (status) => {
  const statusMap = {
    pending: '待付款',
    paid: '待发货',
    shipped: '待收货',
    completed: '已完成',
    cancelled: '已取消'
  }
  return statusMap[status] || status
}

const getStatusColor = (status) => {
  const colorMap = {
    pending: 'text-orange-500',
    paid: 'text-blue-500',
    shipped: 'text-purple-500',
    completed: 'text-green-500',
    cancelled: 'text-gray-500'
  }
  return colorMap[status] || 'text-gray-500'
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return `${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${String(date.getMinutes()).padStart(2, '0')}`
}

const goToOrderDetail = (orderId) => {
  router.push(`/order/${orderId}`)
}

const cancelOrder = (orderId) => {
  if (confirm('确定要取消这个订单吗？')) {
    cartStore.cancelOrder(orderId)
  }
}
</script>
