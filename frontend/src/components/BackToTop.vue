<template>
  <transition name="fade">
    <button
      v-show="visible"
      @click="scrollToTop"
      class="back-to-top fixed bottom-6 right-6 w-12 h-12 bg-gradient-to-r from-primary to-accent text-white rounded-full shadow-lg flex items-center justify-center z-50"
    >
      <i class="fas fa-arrow-up"></i>
    </button>
  </transition>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const visible = ref(false)

const handleScroll = () => {
  visible.value = window.scrollY > 300
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>
