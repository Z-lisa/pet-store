<template>
  <section id="services" class="py-8 px-4 bg-soft/50">
    <transition name="slide-up">
      <div v-show="true">
        <div class="text-center mb-6">
          <h2 class="section-title text-2xl font-bold text-gray-800 mb-2">服务项目</h2>
          <p class="text-gray-500 mt-4">专业呵护，全方位照顾</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div
            v-for="service in services"
            :key="service.id"
            class="service-card bg-white rounded-2xl p-6 card-hover shadow-md"
          >
            <div class="flex items-start mb-4">
              <div
                class="service-icon w-14 h-14 rounded-full flex items-center justify-center text-white text-2xl mr-4"
                :class="service.color"
              >
                <i :class="service.icon"></i>
              </div>
              <div class="flex-1">
                <h3 class="text-lg font-bold text-gray-800 mb-1">{{ service.name }}</h3>
                <span class="inline-block bg-warm text-gray-600 text-xs px-2 py-1 rounded-full">
                  {{ service.duration }}
                </span>
              </div>
            </div>
            <p class="text-gray-600 text-sm mb-3 leading-relaxed">{{ service.description }}</p>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="highlight in service.highlights"
                :key="highlight"
                class="text-xs px-2 py-1 bg-soft rounded-full text-secondary font-medium"
              >
                {{ highlight }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </section>
</template>

<script setup>
const services = [
  {
    id: 1,
    name: '宠物洗护',
    description: '专业洗护流程，使用天然无害洗护产品，深层清洁毛发，去除异味，让爱宠焕然一新。',
    highlights: ['药浴护理', '皮肤检查', '耳道清洁', '指甲修剪'],
    icon: 'fas fa-shower',
    color: 'bg-gradient-to-br from-blue-400 to-blue-600',
    duration: '60-90 分钟'
  },
  {
    id: 2,
    name: '美容造型',
    description: '资深美容师根据宠物品种特点和个人喜好，设计专属造型，修剪毛发，打造萌宠形象。',
    highlights: ['精修造型', '染色设计', 'SPA 护理', '精油按摩'],
    icon: 'fas fa-cut',
    color: 'bg-gradient-to-br from-pink-400 to-pink-600',
    duration: '90-120 分钟'
  },
  {
    id: 3,
    name: '寄养看护',
    description: '宽敞舒适的寄养环境，24 小时监控，定时遛弯互动，让爱宠在主人外出期间也能享受家的温暖。',
    highlights: ['独立空间', '定时喂食', '互动陪伴', '健康观察'],
    icon: 'fas fa-home',
    color: 'bg-gradient-to-br from-green-400 to-green-600',
    duration: '按天计费'
  },
  {
    id: 4,
    name: '疫苗保健',
    description: '提供全套疫苗接种服务，定期健康检查，驱虫防疫，建立健康档案，守护宠物健康。',
    highlights: ['进口疫苗', '体检套餐', '驱虫服务', '健康咨询'],
    icon: 'fas fa-syringe',
    color: 'bg-gradient-to-br from-purple-400 to-purple-600',
    duration: '30-60 分钟'
  }
]
</script>
