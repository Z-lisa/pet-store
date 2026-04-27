<template>
  <section id="booking" class="py-8 px-4">
    <transition name="slide-up">
      <div v-show="true">
        <div class="text-center mb-6">
          <h2 class="section-title text-2xl font-bold text-gray-800 mb-2">在线预约</h2>
          <p class="text-gray-500 mt-4">提前预约，免等待</p>
        </div>

        <div class="bg-white rounded-2xl p-6 card-hover shadow-lg">
          <form @submit.prevent="submitBooking" class="space-y-4">
            <div>
              <label class="block text-gray-700 font-medium mb-2">
                <i class="fas fa-user text-primary mr-2"></i>姓名
              </label>
              <input
                type="text"
                v-model="bookingForm.name"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:border-secondary transition-colors"
                placeholder="请输入您的姓名"
                required
              />
              <p v-if="errors.name" class="text-red-500 text-xs mt-1">{{ errors.name }}</p>
            </div>

            <div>
              <label class="block text-gray-700 font-medium mb-2">
                <i class="fas fa-phone text-secondary mr-2"></i>联系电话
              </label>
              <input
                type="tel"
                v-model="bookingForm.phone"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:border-secondary transition-colors"
                placeholder="请输入手机号码"
                pattern="[0-9]{11}"
                required
              />
              <p v-if="errors.phone" class="text-red-500 text-xs mt-1">{{ errors.phone }}</p>
            </div>

            <div>
              <label class="block text-gray-700 font-medium mb-2">
                <i class="fas fa-paw text-accent mr-2"></i>宠物类型
              </label>
              <select
                v-model="bookingForm.petType"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:border-secondary transition-colors"
                required
              >
                <option value="">请选择宠物类型</option>
                <option v-for="type in petTypes" :key="type" :value="type">{{ type }}</option>
              </select>
              <p v-if="errors.petType" class="text-red-500 text-xs mt-1">{{ errors.petType }}</p>
            </div>

            <div>
              <label class="block text-gray-700 font-medium mb-2">
                <i class="fas fa-spa text-primary mr-2"></i>服务项目
              </label>
              <select
                v-model="bookingForm.service"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:border-secondary transition-colors"
                required
              >
                <option value="">请选择服务项目</option>
                <option v-for="service in serviceList" :key="service.id" :value="service.name">
                  {{ service.name }}
                </option>
              </select>
              <p v-if="errors.service" class="text-red-500 text-xs mt-1">{{ errors.service }}</p>
            </div>

            <div>
              <label class="block text-gray-700 font-medium mb-2">
                <i class="fas fa-calendar text-secondary mr-2"></i>预约日期
              </label>
              <input
                type="date"
                v-model="bookingForm.date"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:border-secondary transition-colors"
                :min="minDate"
                required
              />
              <p v-if="errors.date" class="text-red-500 text-xs mt-1">{{ errors.date }}</p>
            </div>

            <div>
              <label class="block text-gray-700 font-medium mb-2">
                <i class="fas fa-comment-alt text-accent mr-2"></i>备注说明
              </label>
              <textarea
                v-model="bookingForm.remark"
                rows="3"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:border-secondary transition-colors resize-none"
                placeholder="如有特殊需求请在此说明（选填）"
              ></textarea>
            </div>

            <button
              type="submit"
              class="btn-primary w-full py-3 rounded-xl text-white font-bold text-lg shadow-lg mt-6"
            >
              <i class="fas fa-paper-plane mr-2"></i>
              提交预约
            </button>
          </form>
        </div>
      </div>
    </transition>

    <!-- 预约成功提示 -->
    <transition name="fade">
      <div
        v-if="showSuccess"
        class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4"
      >
        <div class="bg-white rounded-2xl p-8 max-w-sm w-full text-center card-hover">
          <div
            class="w-20 h-20 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-4"
          >
            <i class="fas fa-check text-4xl text-green-500"></i>
          </div>
          <h3 class="text-2xl font-bold text-gray-800 mb-2">预约成功！</h3>
          <p class="text-gray-600 mb-6">我们会尽快与您联系确认预约详情</p>
          <button
            @click="showSuccess = false"
            class="btn-primary px-8 py-3 rounded-xl text-white font-bold"
          >
            确定
          </button>
        </div>
      </div>
    </transition>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'

const showSuccess = ref(false)
const bookingForm = ref({
  name: '',
  phone: '',
  petType: '',
  service: '',
  date: '',
  remark: ''
})
const errors = ref({})

const petTypes = ['狗狗', '猫咪', '兔子', '仓鼠', '其他']

const serviceList = [
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

const minDate = computed(() => {
  const today = new Date()
  return today.toISOString().split('T')[0]
})

// 初始化预约日期为明天
const initDate = () => {
  const today = new Date()
  const tomorrow = new Date(today)
  tomorrow.setDate(tomorrow.getDate() + 1)
  bookingForm.value.date = tomorrow.toISOString().split('T')[0]
}

initDate()

const validateForm = () => {
  errors.value = {}

  if (!bookingForm.value.name || bookingForm.value.name.trim().length < 2) {
    errors.value.name = '请输入至少 2 个字符的姓名'
  }

  const phoneRegex = /^1[3-9]\d{9}$/
  if (!bookingForm.value.phone || !phoneRegex.test(bookingForm.value.phone)) {
    errors.value.phone = '请输入正确的 11 位手机号码'
  }

  if (!bookingForm.value.petType) {
    errors.value.petType = '请选择宠物类型'
  }

  if (!bookingForm.value.service) {
    errors.value.service = '请选择服务项目'
  }

  const selectedDate = new Date(bookingForm.value.date)
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  if (selectedDate < today) {
    errors.value.date = '预约日期不能早于今天'
  }

  return Object.keys(errors.value).length === 0
}

const submitBooking = () => {
  if (validateForm()) {
    console.log('预约信息:', bookingForm.value)
    showSuccess.value = true

    bookingForm.value = {
      name: '',
      phone: '',
      petType: '',
      service: '',
      date: '',
      remark: ''
    }

    const tomorrow = new Date()
    tomorrow.setDate(tomorrow.getDate() + 1)
    bookingForm.value.date = tomorrow.toISOString().split('T')[0]
  }
}
</script>
