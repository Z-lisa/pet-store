<template>
  <div class="min-h-screen pb-20">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3">
        <h1 class="text-lg font-bold text-gray-800 text-center">宠物用品</h1>
      </div>
    </header>

    <div class="p-4">
      <!-- 搜索栏 -->
      <div class="relative mb-4">
        <input
          v-model="searchKeyword"
          type="text"
          placeholder="搜索商品..."
          class="w-full pl-10 pr-4 py-3 bg-white rounded-full border border-gray-200 focus:border-secondary"
        >
        <i class="fas fa-search absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
      </div>

      <!-- 分类筛选 -->
      <div class="flex gap-2 mb-4 overflow-x-auto pb-2 scrollbar-hide">
        <button
          v-for="category in categories"
          :key="category.id"
          @click="selectedCategory = category.id"
          class="px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-all"
          :class="selectedCategory === category.id 
            ? 'btn-primary text-white shadow-lg' 
            : 'bg-white text-gray-600 border border-gray-200'"
        >
          {{ category.name }}
        </button>
      </div>

      <!-- 商品列表 -->
      <div class="grid grid-cols-2 gap-4">
        <div
          v-for="product in filteredProducts"
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
            <h3 class="font-bold text-gray-800 text-sm mb-1 truncate">{{ product.name }}</h3>
            <p class="text-gray-500 text-xs mb-2 line-clamp-2">{{ product.description }}</p>
            <div class="flex items-center justify-between">
              <span class="text-accent font-bold">¥{{ product.price }}</span>
              <button 
                @click.stop="addToCart(product)"
                class="w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center text-primary hover:bg-primary hover:text-white transition-all"
              >
                <i class="fas fa-cart-plus text-xs"></i>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 无结果提示 -->
      <div v-if="filteredProducts.length === 0" class="text-center py-12">
        <i class="fas fa-search text-4xl text-gray-300 mb-4"></i>
        <p class="text-gray-500">没有找到相关商品</p>
      </div>
    </div>

    <!-- 添加成功提示 -->
    <transition name="fade">
      <div 
        v-if="showSuccess" 
        class="fixed top-20 left-1/2 transform -translate-x-1/2 bg-green-500 text-white px-6 py-3 rounded-full shadow-lg z-50 flex items-center"
      >
        <i class="fas fa-check-circle mr-2"></i>
        已添加到购物车
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

const selectedCategory = ref('all')
const searchKeyword = ref('')
const showSuccess = ref(false)

const categories = [
  { id: 'all', name: '全部' },
  { id: 'food', name: '食品' },
  { id: 'toy', name: '玩具' },
  { id: 'bed', name: '窝垫' },
  { id: 'clothes', name: '服饰' }
]

const products = [
  {
    id: 1,
    name: '天然狗粮',
    description: '进口天然食材，无谷物配方，富含蛋白质',
    price: 168,
    category: 'food',
    image: 'https://images.unsplash.com/photo-1589924691195-41432c84c161?w=300',
    hot: true
  },
  {
    id: 2,
    name: '猫罐头套装',
    description: '多种口味组合，营养丰富，适口性佳',
    price: 89,
    category: 'food',
    image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300',
    hot: true
  },
  {
    id: 3,
    name: '宠物咬胶',
    description: '耐咬磨牙，清洁牙齿，安全无毒',
    price: 35,
    category: 'toy',
    image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1497?w=300',
    hot: false
  },
  {
    id: 4,
    name: '互动球玩具',
    description: '智能滚动，自动避障，增加运动量',
    price: 128,
    category: 'toy',
    image: 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=300',
    hot: true
  },
  {
    id: 5,
    name: '宠物窝垫',
    description: '柔软舒适，可拆洗，四季通用',
    price: 158,
    category: 'bed',
    image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=300',
    hot: false
  },
  {
    id: 6,
    name: '保暖宠物窝',
    description: '加厚保暖，防风防水，冬季必备',
    price: 228,
    category: 'bed',
    image: 'https://images.unsplash.com/photo-1597843786271-105124152c92?w=300',
    hot: true
  },
  {
    id: 7,
    name: '宠物毛衣',
    description: '纯棉材质，保暖透气，多色可选',
    price: 78,
    category: 'clothes',
    image: 'https://images.unsplash.com/photo-1560743641-3914f2c45636?w=300',
    hot: false
  },
  {
    id: 8,
    name: '宠物雨衣',
    description: '防水透气，反光条设计，安全出行',
    price: 98,
    category: 'clothes',
    image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=300',
    hot: false
  }
]

const filteredProducts = computed(() => {
  let result = products
  
  if (selectedCategory.value !== 'all') {
    result = result.filter(p => p.category === selectedCategory.value)
  }
  
  if (searchKeyword.value) {
    const keyword = searchKeyword.value.toLowerCase()
    result = result.filter(p => 
      p.name.toLowerCase().includes(keyword) ||
      p.description.toLowerCase().includes(keyword)
    )
  }
  
  return result
})

const goToDetail = (id) => {
  router.push(`/product/${id}`)
}

const addToCart = (product) => {
  cartStore.addToCart(product)
  showSuccess.value = true
  setTimeout(() => {
    showSuccess.value = false
  }, 2000)
}
</script>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
