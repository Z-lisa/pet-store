<template>
  <div class="min-h-screen bg-gray-50 pb-20">
    <!-- 头部 -->
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3 flex items-center">
        <button @click="$router.back()" class="mr-4">
          <i class="fas fa-arrow-left text-gray-600"></i>
        </button>
        <h1 class="text-lg font-bold text-gray-800">订单详情</h1>
      </div>
    </header>

    <div v-if="order">
      <!-- 订单状态 -->
      <section class="bg-gradient-to-r from-primary to-secondary m-4 rounded-2xl p-6 text-white">
        <div class="flex items-center mb-2">
          <i class="fas fa-check-circle text-2xl mr-3"></i>
          <span class="text-xl font-bold">{{ getStatusText(order.status) }}</span>
        </div>
        <p class="text-white/80 text-sm">
          {{ getStatusDesc(order.status) }}
        </p>
      </section>

      <!-- 物流信息 -->
      <section v-if="order.status === 'shipped'" class="bg-white m-4 rounded-2xl p-4 shadow-sm">
        <div class="flex items-center">
          <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center mr-3">
            <i class="fas fa-truck text-blue-500"></i>
          </div>
          <div class="flex-1">
            <p class="font-medium text-gray-800">运输中</p>
            <p class="text-gray-500 text-sm">预计明天送达</p>
          </div>
          <i class="fas fa-chevron-right text-gray-400"></i>
        </div>
      </section>

      <!-- 收货地址 -->
      <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
        <div class="flex items-start">
          <i class="fas fa-map-marker-alt text-accent mt-1 mr-3"></i>
          <div>
            <p class="font-medium text-gray-800">
              {{ order.address.name }} {{ order.address.phone }}
            </p>
            <p class="text-gray-500 text-sm mt-1">{{ order.address.detail }}</p>
          </div>
        </div>
      </section>

      <!-- 商品信息 -->
      <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
        <h2 class="font-bold text-gray-800 mb-4">商品信息</h2>
        <div class="space-y-4">
          <div
            v-for="item in order.items"
            :key="item.id"
            class="flex gap-4"
          >
            <img :src="item.image" :alt="item.name" class="w-20 h-20 object-cover rounded-xl">
            <div class="flex-1">
              <h3 class="font-medium text-gray-800">{{ item.name }}</h3>
              <p v-if="item.spec" class="text-gray-500 text-sm">规格: {{ item.spec }}</p>
              <div class="flex justify-between items-center mt-2">
                <span class="text-accent font-bold">¥{{ item.price }}</span>
                <span class="text-gray-500">x{{ item.quantity }}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 价格明细 -->
      <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
        <h2 class="font-bold text-gray-800 mb-4">价格明细</h2>
        <div class="space-y-2 text-sm">
          <div class="flex justify-between">
            <span class="text-gray-500">商品总价</span>
            <span class="text-gray-800">¥{{ order.totalPrice }}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500">运费</span>
            <span class="text-gray-800">¥{{ order.shippingPrice }}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500">优惠</span>
            <span class="text-red-500">-¥{{ order.discount }}</span>
          </div>
          <div class="border-t pt-2 mt-2">
            <div class="flex justify-between">
              <span class="font-bold text-gray-800">实付金额</span>
              <span class="text-xl font-bold text-accent">¥{{ order.totalPrice + order.shippingPrice - order.discount }}</span>
            </div>
          </div>
        </div>
      </section>

      <!-- 订单信息 -->
      <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
        <h2 class="font-bold text-gray-800 mb-4">订单信息</h2>
        <div class="space-y-2 text-sm text-gray-500">
          <p>订单编号: {{ order.id }}</p>
          <p>下单时间: {{ formatDate(order.createdAt) }}</p>
          <p>配送方式: {{ getShippingMethod(order.shippingMethod) }}</p>
          <p v-if="order.remark">订单备注: {{ order.remark }}</p>
        </div>
      </section>

      <!-- 底部操作栏 -->
      <div class="fixed bottom-0 left-0 right-0 bg-white border-t px-4 py-3 flex justify-end gap-3 max-w-3xl mx-auto">
        <button 
          v-if="order.status === 'pending'"
          @click="cancelOrder"
          class="px-6 py-2 rounded-full border border-gray-300 text-gray-600"
        >
          取消订单
        </button>
        <button 
          v-if="order.status === 'pending'"
          class="btn-primary px-6 py-2 rounded-full text-white font-medium"
        >
          立即支付
        </button>
        <button 
          v-if="order.status === 'shipped'"
          class="btn-primary px-6 py-2 rounded-full text-white font-medium"
        >
          确认收货
        </button>
        <button 
          v-if="order.status === 'completed'"
          class="px-6 py-2 rounded-full border border-gray-300 text-gray-600"
        >
          申请售后
        </button>
      </div>
    </div>

    <!-- 订单不存在 -->
    <div v-else class="flex flex-col items-center justify-center py-20">
      <i class="fas fa-exclamation-circle text-6xl text-gray-300 mb-4"></i>
      <p class="text-gray-500 mb-4">订单不存在</p>
      <router-link 
        to="/orders" 
        class="btn-primary px-6 py-3 rounded-full text-white font-bold"
      >
        返回订单列表
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const route = useRoute()
const router = useRouter()
const cartStore = useCartStore()

const order = computed(() => {
  return cartStore.getOrderById(route.params.id)
})

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

const getStatusDesc = (status) => {
  const descMap = {
    pending: '请在30分钟内完成支付',
    paid: '商家正在为您准备商品',
    shipped: '商品正在运输中，请耐心等待',
    completed: '订单已完成，期待您的再次光临',
    cancelled: '订单已取消，欢迎再次购买'
  }
  return descMap[status] || ''
}

const getShippingMethod = (method) => {
  const methodMap = {
    express: '快递配送',
    sameDay: '同城配送',
    selfPickup: '到店自取'
  }
  return methodMap[method] || method
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`
}

const cancelOrder = () => {
  if (confirm('确定要取消这个订单吗？')) {
    cartStore.cancelOrder(order.value.id)
  }
}
</script>
