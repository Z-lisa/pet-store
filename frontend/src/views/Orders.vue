<template>
  <div class="min-h-screen pb-20">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3">
        <h1 class="text-lg font-bold text-gray-800 text-center">我的订单</h1>
      </div>
    </header>

    <div class="p-4">
      <!-- 加载状态 -->
      <div v-if="loading" class="flex justify-center py-12">
        <i class="fas fa-spinner fa-spin text-3xl text-primary"></i>
      </div>

      <!-- 空订单 -->
      <div v-else-if="orders.length === 0" class="text-center py-16">
        <i class="fas fa-clipboard-list text-6xl text-gray-300 mb-4"></i>
        <p class="text-gray-500 mb-6">暂无订单</p>
        <router-link to="/products" class="btn-primary inline-block px-8 py-3 rounded-full text-white font-bold">
          去购物
        </router-link>
      </div>

      <!-- 订单列表 -->
      <div v-else class="space-y-4">
        <div
          v-for="order in orders"
          :key="order.id"
          class="bg-white rounded-2xl p-4 shadow-md"
        >
          <div class="flex justify-between items-center mb-3 pb-3 border-b">
            <span class="text-gray-500 text-sm">订单号: {{ order.id }}</span>
            <span
              class="text-sm font-medium px-2 py-1 rounded-full"
              :class="getStatusClass(order.status)"
            >
              {{ getStatusText(order.status) }}
            </span>
          </div>

          <div class="space-y-2 mb-3">
            <div
              v-for="item in order.items"
              :key="item.id"
              class="flex items-center gap-3"
            >
              <img :src="item.image" :alt="item.name" class="w-16 h-16 object-cover rounded-lg">
              <div class="flex-1">
                <h4 class="font-medium text-gray-800 text-sm">{{ item.name }}</h4>
                <p class="text-gray-500 text-xs">x{{ item.quantity }}</p>
              </div>
              <span class="text-gray-800 font-medium">¥{{ item.price * item.quantity }}</span>
            </div>
          </div>

          <div class="flex justify-between items-center pt-3 border-t">
            <span class="text-gray-500 text-sm">{{ formatDate(order.created_at) }}</span>
            <span class="font-bold text-gray-800">合计: ¥{{ order.total_amount }}</span>
          </div>

          <div class="flex gap-2 mt-3">
            <button
              v-if="order.status === 'pending'"
              @click="cancelOrder(order.id)"
              class="flex-1 py-2 border border-gray-200 rounded-lg text-gray-600 text-sm font-medium"
            >
              取消订单
            </button>
            <button
              v-if="order.status === 'pending'"
              class="flex-1 py-2 bg-primary text-white rounded-lg text-sm font-medium"
            >
              立即支付
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useAppStore } from '@/stores/app'

const appStore = useAppStore()

const loading = computed(() => appStore.loading)
const orders = computed(() => appStore.orders)

const getStatusText = (status) => {
  const statusMap = {
    pending: '待付款',
    paid: '已支付',
    processing: '处理中',
    shipped: '已发货',
    completed: '已完成',
    cancelled: '已取消'
  }
  return statusMap[status] || status
}

const getStatusClass = (status) => {
  const classMap = {
    pending: 'bg-yellow-100 text-yellow-700',
    paid: 'bg-blue-100 text-blue-700',
    processing: 'bg-purple-100 text-purple-700',
    shipped: 'bg-indigo-100 text-indigo-700',
    completed: 'bg-green-100 text-green-700',
    cancelled: 'bg-gray-100 text-gray-700'
  }
  return classMap[status] || 'bg-gray-100 text-gray-700'
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const cancelOrder = async (orderId) => {
  if (!confirm('确定要取消该订单吗？')) return

  try {
    await appStore.cancelOrder(orderId)
    alert('订单已取消')
  } catch (error) {
    alert('取消订单失败')
    console.error(error)
  }
}

onMounted(async () => {
  try {
    await appStore.fetchOrders()
  } catch (error) {
    console.error('Failed to load orders:', error)
  }
})
</script>
