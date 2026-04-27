<template>
  <section id="contact" class="py-8 px-4 bg-warm/50">
    <transition name="slide-up">
      <div v-show="true">
        <div class="text-center mb-6">
          <h2 class="section-title text-2xl font-bold text-gray-800 mb-2">联系我们</h2>
          <p class="text-gray-500 mt-4">欢迎到店咨询</p>
        </div>

        <div class="bg-white rounded-2xl p-6 mb-6 card-hover">
          <div class="space-y-4">
            <div class="flex items-start">
              <div
                class="w-10 h-10 rounded-full bg-primary/20 flex items-center justify-center mr-4 flex-shrink-0"
              >
                <i class="fas fa-map-marker-alt text-primary text-lg"></i>
              </div>
              <div class="flex-1">
                <h3 class="font-bold text-gray-800 mb-1">门店地址</h3>
                <p class="text-gray-600">{{ contactInfo.address }}</p>
              </div>
            </div>

            <div class="flex items-start">
              <div
                class="w-10 h-10 rounded-full bg-secondary/20 flex items-center justify-center mr-4 flex-shrink-0"
              >
                <i class="fas fa-phone text-secondary text-lg"></i>
              </div>
              <div class="flex-1">
                <h3 class="font-bold text-gray-800 mb-1">联系电话</h3>
                <p class="text-gray-600">{{ contactInfo.phone }}</p>
                <a :href="'tel:' + contactInfo.phone" class="text-secondary text-sm hover:underline">
                  点击拨打
                </a>
              </div>
            </div>

            <div class="flex items-start">
              <div
                class="w-10 h-10 rounded-full bg-accent/20 flex items-center justify-center mr-4 flex-shrink-0"
              >
                <i class="fas fa-clock text-accent text-lg"></i>
              </div>
              <div class="flex-1">
                <h3 class="font-bold text-gray-800 mb-1">营业时间</h3>
                <p class="text-gray-600">{{ contactInfo.hours }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 地图占位 -->
        <div class="bg-white rounded-2xl overflow-hidden shadow-md mb-6">
          <div
            class="h-48 bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center"
          >
            <div class="text-center">
              <i class="fas fa-map-marked-alt text-4xl text-secondary mb-2"></i>
              <p class="text-gray-600 text-sm">地图加载中...</p>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </section>
</template>

<script setup>
const contactInfo = {
  address: '北京市朝阳区幸福路 88 号温馨宠物店',
  phone: '400-888-6666',
  hours: '周一至周日 9:00-21:00'
}
</script>
