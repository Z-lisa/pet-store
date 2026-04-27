<template>
  <div class="min-h-screen pb-32">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3 flex items-center justify-between">
        <h1 class="text-lg font-bold text-gray-800">购物车</h1>
        <button
          v-if="cartItems.length > 0"
          @click="clearCart"
          class="text-gray-500 text-sm"
        >
          清空
        </button>
      </div>
    </header>

    <div class="p-4">
      <!-- 空购物车 -->
      <div v-if="cartItems.length === 0" class="text-center py-16">
        <i class="fas fa-shopping-cart text-6xl text-gray-300 mb-4"></i>
        <p class="text-gray-500 mb-6">购物车是空的</p>
        <router-link to="/products" class="btn-primary inline-block px-8 py-3 rounded-full text-white font-bold">
          去购物
        </router-link>
      </div>

      <!-- 购物车列表 -->
      <div v-else class="space-y-4">
        <div
          v-for="item in cartItems"
          :key="item.id"
          class="bg-white rounded-2xl p-4 shadow-md flex items-center gap-4"
        >
          <img :src="item.image" :alt="item.name" class="w-20 h-20 object-cover rounded-xl">
          <div class="flex-1">
            <h3 class="font-bold text-gray-800">{{ item.name }}</h3>
            <p class="text-accent font-bold mt-1">¥{{ item.price }}</p>
            <div class="flex items-center gap-3 mt-2">
              <button
                @click="decreaseQuantity(item.id)"
                class="w-8 h-8 rounded-full border border-gray-200 flex items-center justify-center text-gray-600"
              >
                <i class="fas fa-minus text-xs"></i>
              </button>
              <span class="font-medium w-8 text-center">{{ item.quantity }}</span>
              <button
                @click="increaseQuantity(item.id)"
                class="w-8 h-8 rounded-full border border-gray-200 flex items-center justify-center text-gray-600"
              >
                <i class="fas fa-plus text-xs"></i>
              </button>
            </div>
          </div>
          <button
            @click="removeItem(item.id)"
            class="text-gray-400 hover:text-red-500 transition-colors"
          >
            <i class="fas fa-trash-alt"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- 底部结算栏 -->
    <div
      v-if="cartItems.length > 0"
      class="fixed bottom-0 left-0 right-0 bg-white border-t px-4 py-3 flex items-center justify-between max-w-3xl mx-auto"
    >
      <div>
        <p class="text-gray-500 text-sm">合计:</p>
        <p class="text-2xl font-bold text-accent">¥{{ totalPrice }}</p>
      </div>
      <router-link
        to="/checkout"
        class="btn-primary px-8 py-3 rounded-full text-white font-bold shadow-lg"
      >
        去结算 ({{ totalCount }})
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useAppStore } from '@/stores/app'

const appStore = useAppStore()

const cartItems = computed(() => appStore.cartItems)
const totalPrice = computed(() => appStore.totalPrice)
const totalCount = computed(() => appStore.totalItems)

const increaseQuantity = (id) => {
  const item = cartItems.value.find(i => i.id === id)
  if (item) {
    appStore.updateQuantity(id, item.quantity + 1)
  }
}

const decreaseQuantity = (id) => {
  const item = cartItems.value.find(i => i.id === id)
  if (item) {
    appStore.updateQuantity(id, item.quantity - 1)
  }
}

const removeItem = (id) => {
  appStore.removeFromCart(id)
}

const clearCart = () => {
  if (confirm('确定要清空购物车吗？')) {
    appStore.clearCart()
  }
}
</script>
