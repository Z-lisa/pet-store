<template>
  <section id="products" class="py-8 px-4">
    <transition name="slide-up">
      <div v-show="true">
        <div class="text-center mb-6">
          <h2 class="section-title text-2xl font-bold text-gray-800 mb-2">宠物用品</h2>
          <p class="text-gray-500 mt-4">精选好物，品质保证</p>
        </div>

        <!-- 分类筛选 -->
        <div class="flex flex-wrap gap-2 mb-6 justify-center">
          <button
            v-for="category in productCategories"
            :key="category.id"
            @click="selectedCategory = category.id"
            class="px-4 py-2 rounded-full text-sm font-medium transition-all"
            :class="
              selectedCategory === category.id
                ? 'btn-primary text-white shadow-lg'
                : 'bg-white text-gray-600 hover:bg-warm'
            "
          >
            {{ category.name }}
          </button>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          <div
            v-for="product in filteredProducts"
            :key="product.id"
            class="bg-white rounded-2xl overflow-hidden shadow-md card-hover"
          >
            <div class="relative overflow-hidden">
              <img
                :src="product.image"
                :alt="product.name"
                class="w-full h-40 object-cover gallery-img"
              />
              <span
                v-if="product.hot"
                class="absolute top-2 right-2 bg-accent text-white text-xs px-2 py-1 rounded-full"
              >
                <i class="fas fa-fire mr-1"></i>热门
              </span>
            </div>
            <div class="p-3">
              <h3 class="font-bold text-gray-800 text-sm mb-1 truncate">{{ product.name }}</h3>
              <p class="text-gray-500 text-xs mb-2 line-clamp-2">{{ product.description }}</p>
              <div class="flex items-center justify-between">
                <span class="text-accent font-bold text-sm">¥{{ product.price }}</span>
                <button class="text-secondary hover:text-accent transition-colors">
                  <i class="fas fa-shopping-cart"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedCategory = ref('all')

const productCategories = [
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
    price: '168',
    category: 'food',
    image: 'https://images.unsplash.com/photo-1589924691195-41432c84c161?w=300',
    hot: true
  },
  {
    id: 2,
    name: '猫罐头套装',
    description: '多种口味组合，营养丰富，适口性佳',
    price: '89',
    category: 'food',
    image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=300',
    hot: true
  },
  {
    id: 3,
    name: '宠物咬胶',
    description: '耐咬磨牙，清洁牙齿，安全无毒',
    price: '35',
    category: 'toy',
    image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1497?w=300',
    hot: false
  },
  {
    id: 4,
    name: '互动球玩具',
    description: '智能滚动，自动避障，增加运动量',
    price: '128',
    category: 'toy',
    image: 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=300',
    hot: true
  },
  {
    id: 5,
    name: '宠物窝垫',
    description: '柔软舒适，可拆洗，四季通用',
    price: '158',
    category: 'bed',
    image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=300',
    hot: false
  },
  {
    id: 6,
    name: '保暖宠物窝',
    description: '加厚保暖，防风防水，冬季必备',
    price: '228',
    category: 'bed',
    image: 'https://images.unsplash.com/photo-1597843786271-105124152c92?w=300',
    hot: true
  },
  {
    id: 7,
    name: '宠物毛衣',
    description: '纯棉材质，保暖透气，多色可选',
    price: '78',
    category: 'clothes',
    image: 'https://images.unsplash.com/photo-1560743641-3914f2c45636?w=300',
    hot: false
  },
  {
    id: 8,
    name: '雨衣',
    description: '防水透气，反光条设计，安全出行',
    price: '98',
    category: 'clothes',
    image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=300',
    hot: false
  }
]

const filteredProducts = computed(() => {
  if (selectedCategory.value === 'all') {
    return products
  }
  return products.filter((p) => p.category === selectedCategory.value)
})
</script>
