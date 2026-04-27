<template>
  <div class="min-h-screen pb-20">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3">
        <h1 class="text-lg font-bold text-gray-800 text-center">服务项目</h1>
      </div>
    </header>

    <div class="p-4">
      <!-- 加载状态 -->
      <div v-if="loading" class="flex justify-center py-12">
        <i class="fas fa-spinner fa-spin text-3xl text-primary"></i>
      </div>

      <!-- 服务列表 -->
      <div v-else class="space-y-4">
        <div
          v-for="service in services"
          :key="service.id"
          class="bg-white rounded-2xl overflow-hidden shadow-md card-hover"
        >
          <div class="flex items-start p-4">
            <div class="w-20 h-20 rounded-xl flex items-center justify-center text-white text-3xl flex-shrink-0" :class="service.color">
              <i :class="service.icon"></i>
            </div>
            <div class="ml-4 flex-1">
              <div class="flex justify-between items-start">
                <h3 class="font-bold text-gray-800 text-lg">{{ service.name }}</h3>
                <span class="text-accent font-bold">{{ service.price }}</span>
              </div>
              <p class="text-gray-500 text-sm mt-1">{{ service.description }}</p>
              <div class="flex flex-wrap gap-2 mt-2">
                <span
                  v-for="tag in service.tags"
                  :key="tag"
                  class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
          <div class="px-4 pb-4">
            <router-link
              to="/booking"
              class="btn-primary block w-full py-3 rounded-xl text-white font-bold text-center"
            >
              立即预约
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useAppStore } from '@/stores/app'

const appStore = useAppStore()

const loading = computed(() => appStore.loading)
const services = computed(() => appStore.services)

onMounted(async () => {
  try {
    await appStore.fetchServices()
  } catch (error) {
    console.error('Failed to load services:', error)
  }
})
</script>
