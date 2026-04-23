<template>
  <div class="min-h-screen bg-gray-50 pb-32">
    <!-- 头部 -->
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3 flex items-center justify-between">
        <h1 class="text-lg font-bold text-gray-800">购物车</h1>
        <button 
          v-if="!cartStore.isEmpty"
          @click="clearCart"
          class="text-gray-500 text-sm"
        >
          清空
        </button>
      </div>
    </header>

    <!-- 空购物车 -->
    <div v-if="cartStore.isEmpty" class="flex flex-col items-center justify-center py-20">
      <i class="fas fa-shopping-cart text-6xl text-gray-300 mb-4"></i>
      <p class="text-gray-500 mb-4">购物车是空的</p>
      <router-link 
        to="/products" 
        class="btn-primary px-6 py-3 rounded-full text-white font-bold"
      >
        去逛逛
      </router-link>
    </div>

    <!-- 购物车列表 -->
    <div v-else class="px-4 py-4 space-y-4">
      <div
        v-for="item in cartStore.items"
        :key="item.id"
        class="bg-white rounded-2xl p-4 shadow-md flex gap-4"
      >
        <img :src="item.image" :alt="item.name" class="w-24 h-24 object-cover rounded-xl">
        <div class="flex-1 flex flex-col justify-between">
          <div>
            <h3 class="font-bold text-gray-800">{{ item.name }}</h3>
            <p v-if="item.spec" class="text-gray-500 text-sm">规格: {{ item.spec }}</p>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-accent font-bold text-lg">¥{{ item.price }}</span>
            <div class="flex items-center bg-gray-100 rounded-full">
              <button 
                @click="cartStore.updateQuantity(item.id, item.quantity - 1)"
                class="w-8 h-8 flex items-center justify-center text-gray-600"
              >
                <i class="fas fa-minus text-xs"></i>
              </button>
              <span class="w-8 text-center font-medium">{{ item.quantity }}</span>
              <button 
                @click="cartStore.updateQuantity(item.id, item.quantity + 1)"
                class="w-8 h-8 flex items-center justify-center text-gray-600"
              >
                <i class="fas fa-plus text-xs"></i>
              </button>
            </div>
          </div>
        </div>
        <button 
          @click="cartStore.removeFromCart(item.id)"
          class="text-gray-400 hover:text-red-500 self-start"
        >
          <i class="fas fa-trash-alt"></i>
        </button>
      </div>

      <!-- 推荐商品 -->
      <div class="pt-4">
        <h2 class="text-lg font-bold text-gray-800 mb-4">猜你喜欢</h2>
        <div class="grid grid-cols-2 gap-4">
          <div
            v-for="product in recommendProducts"
            :key="product.id"
            class="bg-white rounded-2xl overflow-hidden shadow-md card-hover"
            @click="goToProduct(product.id)"
          >
            <img :src="product.image" :alt="product.name" class="w-full h-32 object-cover">
            <div class="p-3">
              <h3 class="font-bold text-gray-800 text-sm truncate">{{ product.name }}</h3>
              <div class="flex justify-between items-center mt-2">
                <span class="text-accent font-bold">¥{{ product.price }}</span>
                <button 
                  @click.stop="cartStore.addToCart(product)"
                  class="w-7 h-7 rounded-full bg-primary/20 flex items-center justify-center text-primary"
                >
                  <i class="fas fa-plus text-xs"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 底部结算栏 -->
    <div 
      v-if="!cartStore.isEmpty"
      class="fixed bottom-16 left-0 right-0 bg-white border-t px-4 py-3 flex items-center justify-between max-w-3xl mx-auto"
    >
      <div>
        <p class="text-gray-500 text-sm">合计:</p>
        <p class="text-2xl font-bold text-accent">¥{{ cartStore.totalPrice }}</p>
      </div>
      <button 
        @click="goToCheckout"
        class="btn-primary px-8 py-3 rounded-full text-white font-bold shadow-lg"
      >
        去结算 ({{ cartStore.totalItems }})
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const router = useRouter()
const cartStore = useCartStore()

const recommendProducts = [
  {
    id: 3,
    name: '宠物咬胶',
    price: 35,
    image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1497?w=300'
  },
  {
    id: 5,
    name: '宠物窝垫',
    price: 158,
    image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=300'
  }
]

const clearCart = () => {
  if (confirm('确定要清空购物车吗？')) {
    cartStore.clearCart()
  }
}

const goToProduct = (id) => {
  router.push(`/product/${id}`)
}

const goToCheckout = () => {
  router.push('/checkout')
}
</script>
