const API_BASE_URL = 'http://localhost:8000/api/v1'

class ApiService {
  constructor() {
    this.baseURL = API_BASE_URL
  }

  async request(url, options = {}) {
    const fullUrl = `${this.baseURL}${url}`
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      },
      ...options
    }

    if (config.body && typeof config.body === 'object') {
      config.body = JSON.stringify(config.body)
    }

    try {
      const response = await fetch(fullUrl, config)
      
      if (!response.ok) {
        const error = await response.json().catch(() => ({}))
        throw new Error(error.detail || `HTTP ${response.status}: ${response.statusText}`)
      }

      const contentType = response.headers.get('content-type')
      if (contentType && contentType.includes('application/json')) {
        return await response.json()
      }
      return await response.text()
    } catch (error) {
      console.error('API request failed:', error)
      throw error
    }
  }

  // Products
  getProducts(params = {}) {
    const query = new URLSearchParams(params).toString()
    return this.request(`/products/?${query}`)
  }

  getProduct(id) {
    return this.request(`/products/${id}`)
  }

  getCategories() {
    return this.request('/products/categories')
  }

  // Services
  getServices() {
    return this.request('/services/')
  }

  getService(id) {
    return this.request(`/services/${id}`)
  }

  // Orders
  getOrders(params = {}) {
    const query = new URLSearchParams(params).toString()
    return this.request(`/orders/?${query}`)
  }

  getOrder(id) {
    return this.request(`/orders/${id}`)
  }

  createOrder(data) {
    return this.request('/orders/', {
      method: 'POST',
      body: data
    })
  }

  updateOrder(id, data) {
    return this.request(`/orders/${id}`, {
      method: 'PUT',
      body: data
    })
  }

  getOrderStatistics() {
    return this.request('/orders/statistics')
  }

  // Bookings
  getBookings(params = {}) {
    const query = new URLSearchParams(params).toString()
    return this.request(`/bookings/?${query}`)
  }

  createBooking(data) {
    return this.request('/bookings/', {
      method: 'POST',
      body: data
    })
  }
}

export const api = new ApiService()
