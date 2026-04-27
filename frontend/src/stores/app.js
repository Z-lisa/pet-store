import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/services/api'

export const useAppStore = defineStore('app', () => {
  // State
  const products = ref([])
  const services = ref([])
  const orders = ref([])
  const bookings = ref([])
  const categories = ref([])
  const loading = ref(false)
  const error = ref(null)

  // Getters
  const hotProducts = computed(() => products.value.filter(p => p.hot))
  const totalItems = computed(() => {
    return cartItems.value.reduce((sum, item) => sum + item.quantity, 0)
  })
  const totalPrice = computed(() => {
    return cartItems.value.reduce((sum, item) => sum + (item.price * item.quantity), 0)
  })
  const isEmpty = computed(() => cartItems.value.length === 0)

  // Cart state (local storage)
  const cartItems = ref(JSON.parse(localStorage.getItem('cart') || '[]'))

  // Actions - Products
  const fetchProducts = async (params = {}) => {
    loading.value = true
    try {
      const data = await api.getProducts(params)
      products.value = data
      return data
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  const fetchCategories = async () => {
    try {
      const data = await api.getCategories()
      categories.value = data
      return data
    } catch (err) {
      error.value = err.message
      throw err
    }
  }

  // Actions - Services
  const fetchServices = async () => {
    loading.value = true
    try {
      const data = await api.getServices()
      services.value = data
      return data
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  // Actions - Cart
  const addToCart = (product) => {
    const existingItem = cartItems.value.find(item => item.id === product.id)
    if (existingItem) {
      existingItem.quantity++
    } else {
      cartItems.value.push({
        ...product,
        quantity: 1
      })
    }
    saveCart()
  }

  const removeFromCart = (productId) => {
    const index = cartItems.value.findIndex(item => item.id === productId)
    if (index > -1) {
      cartItems.value.splice(index, 1)
    }
    saveCart()
  }

  const updateQuantity = (productId, quantity) => {
    const item = cartItems.value.find(item => item.id === productId)
    if (item) {
      if (quantity <= 0) {
        removeFromCart(productId)
      } else {
        item.quantity = quantity
        saveCart()
      }
    }
  }

  const clearCart = () => {
    cartItems.value = []
    saveCart()
  }

  const saveCart = () => {
    localStorage.setItem('cart', JSON.stringify(cartItems.value))
  }

  // Actions - Orders
  const fetchOrders = async (params = {}) => {
    loading.value = true
    try {
      const data = await api.getOrders(params)
      orders.value = data
      return data
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  const createOrder = async (orderInfo) => {
    const order = {
      items: cartItems.value.map(item => ({
        product_id: item.id,
        name: item.name,
        price: item.price,
        quantity: item.quantity,
        image: item.image,
        spec: item.spec
      })),
      total_price: totalPrice.value,
      ...orderInfo
    }
    
    const data = await api.createOrder(order)
    orders.value.unshift(data)
    clearCart()
    return data
  }

  const cancelOrder = async (orderId) => {
    await api.updateOrder(orderId, { status: 'cancelled' })
    const order = orders.value.find(o => o.id === orderId)
    if (order) {
      order.status = 'cancelled'
    }
  }

  const getOrderById = (orderId) => {
    return orders.value.find(o => o.id == orderId)
  }

  // Actions - Bookings
  const fetchBookings = async () => {
    loading.value = true
    try {
      const data = await api.getBookings()
      bookings.value = data
      return data
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  const createBooking = async (bookingData) => {
    const data = await api.createBooking(bookingData)
    bookings.value.unshift(data)
    return data
  }

  return {
    // State
    products,
    services,
    orders,
    bookings,
    categories,
    cartItems,
    loading,
    error,
    // Getters
    hotProducts,
    totalItems,
    totalPrice,
    isEmpty,
    // Actions
    fetchProducts,
    fetchCategories,
    fetchServices,
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
    fetchOrders,
    createOrder,
    cancelOrder,
    getOrderById,
    fetchBookings,
    createBooking
  }
})
