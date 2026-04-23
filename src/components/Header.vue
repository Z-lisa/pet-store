<template>
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-sm shadow-md">
    <div class="px-4 py-3">
      <div class="flex justify-between items-center">
        <div class="flex items-center space-x-2">
          <i class="fas fa-paw text-2xl text-accent paw-print"></i>
          <h1 class="text-xl font-bold bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
            温馨宠物店
          </h1>
        </div>
        <nav class="hidden md:flex space-x-4">
          <a
            v-for="item in navItems"
            :key="item.id"
            :href="'#' + item.id"
            @click="activeNav = item.id"
            class="nav-item px-3 py-2 rounded-lg hover:bg-warm transition-all"
            :class="{ active: activeNav === item.id }"
          >
            {{ item.name }}
          </a>
        </nav>
        <button @click="toggleMobileMenu" class="md:hidden text-2xl text-gray-600">
          <i :class="mobileMenuOpen ? 'fas fa-times' : 'fas fa-bars'"></i>
        </button>
      </div>

      <!-- 移动端菜单 -->
      <transition name="fade">
        <div v-if="mobileMenuOpen" class="md:hidden mt-3 pb-3 border-t pt-3">
          <a
            v-for="item in navItems"
            :key="item.id"
            :href="'#' + item.id"
            @click="handleNavClick(item.id)"
            class="block px-3 py-2 rounded-lg hover:bg-warm transition-all"
            :class="{ 
              active: activeNav === item.id, 
              'bg-warm': activeNav === item.id 
            }"
          >
            <i :class="item.icon + ' mr-2 w-5 text-center'"></i>
            {{ item.name }}
          </a>
        </div>
      </transition>
    </div>
  </header>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  activeSection: {
    type: String,
    default: 'about'
  }
})

const emit = defineEmits(['update:activeSection'])

const activeNav = ref(props.activeSection)
const mobileMenuOpen = ref(false)

const navItems = [
  { id: 'about', name: '关于我们', icon: 'fas fa-info-circle' },
  { id: 'services', name: '服务项目', icon: 'fas fa-concierge-bell' },
  { id: 'products', name: '宠物用品', icon: 'fas fa-shopping-bag' },
  { id: 'contact', name: '联系我们', icon: 'fas fa-address-card' },
  { id: 'booking', name: '在线预约', icon: 'fas fa-calendar-check' }
]

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const handleNavClick = (id) => {
  activeNav.value = id
  mobileMenuOpen.value = false
  emit('update:activeSection', id)
}

watch(() => props.activeSection, (newVal) => {
  activeNav.value = newVal
})
</script>
