import authUtils from '@/authentication_utilities'
import axios from 'axios'
import router from '@/router'
import { API_URL } from '@/constants'

const baseAxios = {
  baseURL: API_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
}

const insecureAxios = axios.create(baseAxios)
const secureAxios = axios.create(baseAxios)
secureAxios.interceptors.request.use(
  config => {
    config.headers['Authorization'] = `Bearer ${authUtils.getToken()}`
    return config
  },
  undefined
)
secureAxios.interceptors.response.use(
  undefined,
  error => {
    if (error.response.status === 401) {
      // the token has expired. get a new one
      authUtils.clearToken()
      router.push({
        name: 'login',
        query: { redirect: router.currentRoute.fullPath }
      })
    }
    return Promise.reject(error)
  }
)

export default {
  insecureAxios,
  secureAxios
}
