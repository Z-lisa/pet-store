<template>
  <div class="min-h-screen pb-20">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3">
        <h1 class="text-lg font-bold text-gray-800 text-center">联系我们</h1>
      </div>
    </header>

    <div class="p-4">
      <!-- 店铺信息卡片 -->
      <div class="bg-white rounded-2xl p-6 mb-6 card-hover shadow-md">
        <div class="flex items-center justify-center mb-6">
          <div class="w-20 h-20 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center text-white text-3xl">
            <i class="fas fa-paw"></i>
          </div>
        </div>
        <h2 class="text-xl font-bold text-gray-800 text-center mb-2">温馨宠物店</h2>
        <p class="text-gray-500 text-center">用爱呵护每一个小生命</p>
      </div>

      <!-- 联系方式 -->
      <div class="bg-white rounded-2xl p-6 mb-6 card-hover shadow-md">
        <div class="space-y-4">
          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center mr-4 flex-shrink-0">
              <i class="fas fa-map-marker-alt text-primary text-lg"></i>
            </div>
            <div class="flex-1">
              <h3 class="font-bold text-gray-800 mb-1">门店地址</h3>
              <p class="text-gray-600">{{ contactInfo.address }}</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full bg-secondary/20 flex items-center justify-center mr-4 flex-shrink-0">
              <i class="fas fa-phone text-secondary text-lg"></i>
            </div>
            <div class="flex-1">
              <h3 class="font-bold text-gray-800 mb-1">联系电话</h3>
              <p class="text-gray-600">{{ contactInfo.phone }}</p>
              <a :href="'tel:' + contactInfo.phone" class="text-secondary text-sm hover:underline mt-1 inline-block">
                <i class="fas fa-phone-alt mr-1"></i>点击拨打
              </a>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full bg-accent/20 flex items-center justify-center mr-4 flex-shrink-0">
              <i class="fas fa-clock text-accent text-lg"></i>
            </div>
            <div class="flex-1">
              <h3 class="font-bold text-gray-800 mb-1">营业时间</h3>
              <p class="text-gray-600">{{ contactInfo.hours }}</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center mr-4 flex-shrink-0">
              <i class="fab fa-weixin text-green-500 text-lg"></i>
            </div>
            <div class="flex-1">
              <h3 class="font-bold text-gray-800 mb-1">微信公众号</h3>
              <p class="text-gray-600">温馨宠物店</p>
              <p class="text-gray-500 text-sm">扫码关注获取更多优惠</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 地图占位 -->
      <div class="bg-white rounded-2xl overflow-hidden shadow-md mb-6">
        <div class="h-48 bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center">
          <div class="text-center">
            <i class="fas fa-map-marked-alt text-5xl text-secondary mb-3"></i>
            <p class="text-gray-600 font-medium">地图加载中...</p>
            <p class="text-gray-500 text-sm mt-1">北京市朝阳区幸福路88号</p>
          </div>
        </div>
      </div>

      <!-- 快速操作 -->
      <div class="grid grid-cols-2 gap-4">
        <a :href="'tel:' + contactInfo.phone" class="bg-primary text-white rounded-2xl p-4 text-center card-hover">
          <i class="fas fa-phone-alt text-2xl mb-2"></i>
          <p class="font-medium">立即拨打</p>
        </a>
        <router-link to="/booking" class="bg-secondary text-white rounded-2xl p-4 text-center card-hover">
          <i class="fas fa-calendar-check text-2xl mb-2"></i>
          <p class="font-medium">在线预约</p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
const contactInfo = {
  address: '北京市朝阳区幸福路88号温馨宠物店',
  phone: '400-888-6666',
  hours: '周一至周日 9:00-21:00'
}
</script>
