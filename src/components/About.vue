<template>
  <section id="about" class="py-8 px-4">
    <transition name="slide-up">
      <div v-show="true">
        <div class="text-center mb-6">
          <h2 class="section-title text-2xl font-bold text-gray-800 mb-2">关于我们</h2>
          <p class="text-gray-500 mt-4">用爱呵护每一个小生命</p>
        </div>

        <div class="bg-warm rounded-2xl p-6 mb-6 card-hover">
          <h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center">
            <i class="fas fa-store text-accent mr-2"></i>
            店铺简介
          </h3>
          <p class="text-gray-600 leading-relaxed">
            温馨宠物店成立于 2015 年，是一家专注于宠物全方位服务的专业店铺。我们致力于为宠物提供最优质的生活体验，为宠物主人提供最贴心的服务。店内环境温馨舒适，所有设施均采用宠物友好材料，确保毛孩子们的安全与健康。
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
          <div class="bg-soft rounded-2xl p-6 card-hover">
            <h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center">
              <i class="fas fa-heart text-accent mr-2"></i>
              经营理念
            </h3>
            <ul class="space-y-2 text-gray-600">
              <li class="flex items-start">
                <i class="fas fa-check-circle text-primary mt-1 mr-2"></i>
                <span>以宠物健康为首要考虑</span>
              </li>
              <li class="flex items-start">
                <i class="fas fa-check-circle text-primary mt-1 mr-2"></i>
                <span>提供个性化定制服务</span>
              </li>
              <li class="flex items-start">
                <i class="fas fa-check-circle text-primary mt-1 mr-2"></i>
                <span>使用天然无害产品</span>
              </li>
              <li class="flex items-start">
                <i class="fas fa-check-circle text-primary mt-1 mr-2"></i>
                <span>持续培训专业护理团队</span>
              </li>
            </ul>
          </div>

          <div class="bg-warm rounded-2xl p-6 card-hover">
            <h3 class="text-lg font-bold text-gray-800 mb-3 flex items-center">
              <i class="fas fa-star text-accent mr-2"></i>
              服务优势
            </h3>
            <ul class="space-y-2 text-gray-600">
              <li class="flex items-start">
                <i class="fas fa-medal text-secondary mt-1 mr-2"></i>
                <span>5 年以上经验专业护理师</span>
              </li>
              <li class="flex items-start">
                <i class="fas fa-medal text-secondary mt-1 mr-2"></i>
                <span>国际认证洗护产品</span>
              </li>
              <li class="flex items-start">
                <i class="fas fa-medal text-secondary mt-1 mr-2"></i>
                <span>24 小时监控系统</span>
              </li>
              <li class="flex items-start">
                <i class="fas fa-medal text-secondary mt-1 mr-2"></i>
                <span>一对一专属服务</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- 店铺环境图 -->
        <div class="mb-6">
          <h3 class="text-lg font-bold text-gray-800 mb-4 text-center">店铺环境</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
            <div
              v-for="(image, index) in shopImages"
              :key="index"
              class="relative overflow-hidden rounded-xl shadow-md gallery-img cursor-pointer"
              @click="openGallery(index)"
            >
              <img :src="image.src" :alt="image.alt" class="w-full h-40 object-cover" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent opacity-0 hover:opacity-100 transition-opacity flex items-end p-3">
                <p class="text-white text-sm font-medium">{{ image.alt }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <!-- 图片查看器 -->
    <transition name="fade">
      <div
        v-if="galleryOpen"
        @click="closeGallery"
        class="fixed inset-0 bg-black/90 z-50 flex items-center justify-center p-4"
      >
        <button @click.stop="closeGallery" class="absolute top-4 right-4 text-white text-3xl">
          <i class="fas fa-times"></i>
        </button>
        <img
          :src="shopImages[currentImageIndex].src"
          :alt="shopImages[currentImageIndex].alt"
          class="max-w-full max-h-full object-contain rounded-lg"
        />
        <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 text-white text-center">
          <p class="text-lg font-medium">{{ shopImages[currentImageIndex].alt }}</p>
          <p class="text-sm text-gray-300 mt-1">{{ currentImageIndex + 1 }} / {{ shopImages.length }}</p>
        </div>
      </div>
    </transition>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const shopImages = [
  { src: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400', alt: '店铺前台' },
  { src: 'https://images.unsplash.com/photo-1599141015527-e5a649d675c9?w=400', alt: '洗护区域' },
  { src: 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400', alt: '宠物活动区' },
  { src: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400', alt: '休息区' },
  { src: 'https://images.unsplash.com/photo-1597843786271-105124152c92?w=400', alt: '美容室' },
  { src: 'https://images.unsplash.com/photo-1560743641-3914f2c45636?w=400', alt: '宠物友好环境' }
]

const galleryOpen = ref(false)
const currentImageIndex = ref(0)

const openGallery = (index) => {
  currentImageIndex.value = index
  galleryOpen.value = true
}

const closeGallery = () => {
  galleryOpen.value = false
}
</script>
