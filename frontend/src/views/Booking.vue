<template>
  <div class="min-h-screen pb-20">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="px-4 py-3">
        <h1 class="text-lg font-bold text-gray-800 text-center">在线预约</h1>
      </div>
    </header>

    <div class="p-4">
      <div class="bg-white rounded-2xl p-6 card-hover shadow-lg">
        <form @submit.prevent="submitBooking" class="space-y-5">
          <!-- 宠物主人信息 -->
          <div class="border-b pb-4 mb-4">
            <h3 class="font-bold text-gray-800 mb-3 flex items-center">
              <i class="fas fa-user-circle text-primary mr-2"></i>
              宠物主人信息
            </h3>

            <div class="space-y-4">
              <div>
                <label class="block text-gray-700 font-medium mb-2">姓名</label>
                <input
                  type="text"
                  v-model="bookingForm.name"
                  class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:border-secondary transition-colors"
                  placeholder="请输入您的姓名"
                  required
                />
                <p v-if="errors.name" class="text-red-500 text-xs mt-1">{{ errors.name }}</p>
              </div>

              <div>
                <label class="block text-gray-700 font-medium mb-2">联系电话</label>
                <input
                  type="tel"
                  v-model="bookingForm.phone"
                  class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:border-secondary transition-colors"
                  placeholder="请输入手机号码"
                  required
                />
                <p v-if="errors.phone" class="text-red-500 text-xs mt-1">{{ errors.phone }}</p>
              </div>
            </div>
          </div>

          <!-- 宠物信息 -->
          <div class="border-b pb-4 mb-4">
            <h3 class="font-bold text-gray-800 mb-3 flex items-center">
              <i class="fas fa-paw text-accent mr-2"></i>
              宠物信息
            </h3>

            <div class="space-y-4">
              <div>
                <label class="block text-gray-700 font-medium mb-2">宠物类型</label>
                <div class="grid grid-cols-3 gap-3">
                  <button
                    v-for="type in petTypes"
                    :key="type"
                    type="button"
                    @click="bookingForm.petType = type"
                    class="py-3 rounded-xl border-2 transition-all"
                    :class="bookingForm.petType === type
                      ? 'border-primary bg-primary/10 text-primary font-medium'
                      : 'border-gray-200 text-gray-600'"
                  >
                    {{ type }}
                  </button>
                </div>
                <p v-if="errors.petType" class="text-red-500 text-xs mt-1">{{ errors.petType }}</p>
              </div>

              <div>
                <label class="block text-gray-700 font-medium mb-2">宠物名字</label>
                <input
                  type="text"
                  v-model="bookingForm.petName"
                  class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:border-secondary transition-colors"
                  placeholder="请输入宠物名字"
                />
              </div>
            </div>
          </div>

          <!-- 预约信息 -->
          <div>
            <h3 class="font-bold text-gray-800 mb-3 flex items-center">
              <i class="fas fa-calendar-alt text-secondary mr-2"></i>
              预约信息
            </h3>

            <div class="space-y-4">
              <div>
                <label class="block text-gray-700 font-medium mb-2">服务项目</label>
                <select
                  v-model="bookingForm.service"
                  class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:border-secondary transition-colors"
                  required
                >
                  <option value="">请选择服务项目</option>
                  <option v-for="service in services" :key="service.id" :value="service.name">
                    {{ service.name }} - {{ service.price }}
                  </option>
                </select>
                <p v-if="errors.service" class="text-red-500 text-xs mt-1">{{ errors.service }}</p>
              </div>

              <div>
                <label class="block text-gray-700 font-medium mb-2">预约日期</label>
                <input
                  type="date"
                  v-model="bookingForm.date"
                  class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:border-secondary transition-colors"
                  :min="minDate"
                  required
                />
                <p v-if="errors.date" class="text-red-500 text-xs mt-1">{{ errors.date }}</p>
              </div>

              <div>
                <label class="block text-gray-700 font-medium mb-2">预约时间</label>
                <div class="grid grid-cols-4 gap-2">
                  <button
                    v-for="time in timeSlots"
                    :key="time"
                    type="button"
                    @click="bookingForm.time = time"
                    class="py-2 rounded-lg border-2 text-sm transition-all"
                    :class="bookingForm.time === time
                      ? 'border-primary bg-primary/10 text-primary'
                      : 'border-gray-200 text-gray-600'"
                  >
                    {{ time }}
                  </button>
                </div>
              </div>

              <div>
                <label class="block text-gray-700 font-medium mb-2">备注说明</label>
                <textarea
                  v-model="bookingForm.remark"
                  rows="3"
                  class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:border-secondary transition-colors resize-none"
                  placeholder="如有特殊需求请在此说明（选填）"
                ></textarea>
              </div>
            </div>
          </div>

          <button
            type="submit"
            :disabled="submitting"
            class="btn-primary w-full py-4 rounded-xl text-white font-bold text-lg shadow-lg mt-6 disabled:opacity-50"
          >
            <i class="fas fa-paper-plane mr-2"></i>
            {{ submitting ? '提交中...' : '提交预约' }}
          </button>
        </form>
      </div>

      <!-- 温馨提示 -->
      <div class="mt-6 bg-warm rounded-2xl p-4">
        <h4 class="font-bold text-gray-800 mb-2 flex items-center">
          <i class="fas fa-info-circle text-primary mr-2"></i>
          温馨提示
        </h4>
        <ul class="text-gray-600 text-sm space-y-1">
          <li>• 请提前24小时预约</li>
          <li>• 如需取消请提前2小时告知</li>
          <li>• 首次到店请携带宠物疫苗本</li>
          <li>• 如有疑问请拨打 400-888-6666</li>
        </ul>
      </div>
    </div>

    <!-- 预约成功提示 -->
    <transition name="fade">
      <div
        v-if="showSuccess"
        class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4"
      >
        <div class="bg-white rounded-2xl p-8 max-w-sm w-full text-center">
          <div class="w-20 h-20 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-4">
            <i class="fas fa-check text-4xl text-green-500"></i>
          </div>
          <h3 class="text-2xl font-bold text-gray-800 mb-2">预约成功！</h3>
          <p class="text-gray-600 mb-2">我们会尽快与您联系确认预约详情</p>
          <p class="text-gray-500 text-sm mb-6">预约编号: {{ bookingId }}</p>
          <div class="space-y-3">
            <button
              @click="showSuccess = false"
              class="btn-primary w-full py-3 rounded-xl text-white font-bold"
            >
              确定
            </button>
            <router-link
              to="/"
              class="block w-full py-3 rounded-xl text-gray-600 font-medium border-2 border-gray-200"
            >
              返回首页
            </router-link>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAppStore } from '@/stores/app'

const appStore = useAppStore()

const services = computed(() => appStore.services)

const bookingForm = ref({
  name: '',
  phone: '',
  petType: '',
  petName: '',
  service: '',
  date: '',
  time: '',
  remark: ''
})

const errors = ref({})
const showSuccess = ref(false)
const bookingId = ref('')
const submitting = ref(false)

const petTypes = ['狗狗', '猫咪', '其他']

const timeSlots = [
  '09:00', '10:00', '11:00',
  '14:00', '15:00', '16:00', '17:00'
]

const minDate = computed(() => {
  const today = new Date()
  return today.toISOString().split('T')[0]
})

const validateForm = () => {
  errors.value = {}
  let valid = true

  if (!bookingForm.value.name.trim()) {
    errors.value.name = '请输入姓名'
    valid = false
  }

  if (!bookingForm.value.phone.trim()) {
    errors.value.phone = '请输入联系电话'
    valid = false
  } else if (!/^1[3-9]\d{9}$/.test(bookingForm.value.phone)) {
    errors.value.phone = '请输入正确的手机号码'
    valid = false
  }

  if (!bookingForm.value.petType) {
    errors.value.petType = '请选择宠物类型'
    valid = false
  }

  if (!bookingForm.value.service) {
    errors.value.service = '请选择服务项目'
    valid = false
  }

  if (!bookingForm.value.date) {
    errors.value.date = '请选择预约日期'
    valid = false
  }

  return valid
}

const submitBooking = async () => {
  if (!validateForm()) return
  if (submitting.value) return

  submitting.value = true
  try {
    const result = await appStore.createBooking(bookingForm.value)
    bookingId.value = result.id
    showSuccess.value = true

    // Reset form
    bookingForm.value = {
      name: '',
      phone: '',
      petType: '',
      petName: '',
      service: '',
      date: '',
      time: '',
      remark: ''
    }
  } catch (error) {
    alert('预约提交失败，请重试')
    console.error(error)
  } finally {
    submitting.value = false
  }
}

onMounted(async () => {
  try {
    await appStore.fetchServices()
  } catch (error) {
    console.error('Failed to load services:', error)
  }
})
</script>
