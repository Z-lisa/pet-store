<template>
  <div class="min-h-screen bg-gray-50 pb-32">
    <!-- 头部 -->
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3 flex items-center">
        <button @click="$router.back()" class="mr-4">
          <i class="fas fa-arrow-left text-gray-600"></i>
        </button>
        <h1 class="text-lg font-bold text-gray-800">确认订单</h1>
      </div>
    </header>

    <!-- 收货地址 -->
    <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
      <div class="flex items-center justify-between mb-4">
        <h2 class="font-bold text-gray-800">收货地址</h2>
        <button class="text-secondary text-sm">更换</button>
      </div>
      <div v-if="address" class="flex items-start">
        <i class="fas fa-map-marker-alt text-accent mt-1 mr-3"></i>
        <div>
          <p class="font-medium text-gray-800">{{ address.name }} {{ address.phone }}</p>
          <p class="text-gray-500 text-sm mt-1">{{ address.detail }}</p>
        </div>
      </div>
      <button v-else class="w-full py-4 border-2 border-dashed border-gray-300 rounded-xl text-gray-500">
        <i class="fas fa-plus mr-2"></i>添加收货地址
      </button>
    </section>

    <!-- 商品列表 -->
    <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
      <h2 class="font-bold text-gray-800 mb-4">商品信息</h2>
      <div class="space-y-4">
        <div
          v-for="item in cartStore.items"
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

    <!-- 配送方式 -->
    <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
      <h2 class="font-bold text-gray-800 mb-4">配送方式</h2>
      <div class="space-y-2">
        <label
          v-for="method in shippingMethods"
          :key="method.id"
          class="flex items-center p-3 border-2 rounded-xl cursor-pointer transition-all"
          :class="selectedShipping === method.id ? 'border-primary bg-primary/5' : 'border-gray-200'"
        >
          <input 
            type="radio" 
            :value="method.id" 
            v-model="selectedShipping"
            class="hidden"
          >
          <div class="flex-1">
            <p class="font-medium text-gray-800">{{ method.name }}</p>
            <p class="text-gray-500 text-sm">{{ method.desc }}</p>
          </div>
          <span class="text-gray-800 font-medium">¥{{ method.price }}</span>
        </label>
      </div>
    </section>

    <!-- 备注 -->
    <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
      <h2 class="font-bold text-gray-800 mb-4">订单备注</h2>
      <textarea
        v-model="remark"
        rows="3"
        placeholder="请输入备注信息（选填）"
        class="w-full px-4 py-3 border border-gray-200 rounded-xl resize-none focus:border-secondary"
      ></textarea>
    </section>

    <!-- 价格明细 -->
    <section class="bg-white m-4 rounded-2xl p-4 shadow-sm">
      <h2 class="font-bold text-gray-800 mb-4">价格明细</h2>
      <div class="space-y-2 text-sm">
        <div class="flex justify-between">
          <span class="text-gray-500">商品总价</span>
          <span class="text-gray-800">¥{{ cartStore.totalPrice }}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">运费</span>
          <span class="text-gray-800">¥{{ shippingPrice }}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">优惠</span>
          <span class="text-red-500">-¥{{ discount }}</span>
        </div>
        <div class="border-t pt-2 mt-2">
          <div class="flex justify-between">
            <span class="font-bold text-gray-800">实付金额</span>
            <span class="text-2xl font-bold text-accent">¥{{ finalPrice }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 底部提交栏 -->
    <div class="fixed bottom-0 left-0 right-0 bg-white border-t px-4 py-3 flex items-center justify-between max-w-3xl mx-auto">
      <div>
        <p class="text-gray-500 text-sm">实付:</p>
        <p class="text-2xl font-bold text-accent">¥{{ finalPrice }}</p>
      </div>
      <button 
        @click="submitOrder"
        class="btn-primary px-8 py-3 rounded-full text-white font-bold shadow-lg"
      >
        提交订单
      </button>
    </div>

    <!-- 订单成功弹窗 -->
    <transition name="fade">
      <div v-if="showSuccess" class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl p-8 max-w-sm w-full text-center">
          <div class="w-20 h-20 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-4">
            <i class="fas fa-check text-4xl text-green-500"></i>
          </div>
          <h3 class="text-2xl font-bold text-gray-800 mb-2">订单提交成功!</h3>
          <p class="text-gray-600 mb-6">订单号: {{ createdOrder?.id }}</p>
          <div class="space-y-3">
            <router-link 
              :to="`/order/${createdOrder?.id}`"
              class="btn-primary block w-full py-3 rounded-xl text-white font-bold"
            >
              查看订单
            </router-link>
            <router-link 
              to="/products"
              class="block w-full py-3 rounded-xl text-gray-600 font-medium border-2 border-gray-200"
            >
              继续购物
            </router-link>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cartStore = useCartStore()

const remark = ref('')
const selectedShipping = ref('express')
const showSuccess = ref(false)
const createdOrder = ref(null)

const address = ref({
  name: '张三',
  phone: '138****8888',
  detail: '北京市朝阳区幸福路88号温馨宠物店'
})

const shippingMethods = [
  { id: 'express', name: '快递配送', desc: '预计2-3天送达', price: 10 },
  { id: 'sameDay', name: '同城配送', desc: '当日送达', price: 20 },
  { id: 'selfPickup', name: '到店自取', desc: '下单后到门店取货', price: 0 }
]

const shippingPrice = computed(() => {
  const method = shippingMethods.find(m => m.id === selectedShipping.value)
  return method ? method.price : 0
})

const discount = computed(() => {
  return cartStore.totalPrice >= 199 ? 20 : 0
})

const finalPrice = computed(() => {
  return cartStore.totalPrice + shippingPrice.value - discount.value
})

const submitOrder = () => {
  const order = cartStore.createOrder({
    address: address.value,
    shippingMethod: selectedShipping.value,
    shippingPrice: shippingPrice.value,
    discount: discount.value,
    remark: remark.value
  })
  
  createdOrder.value = order
  showSuccess.value = true
}
</script>
