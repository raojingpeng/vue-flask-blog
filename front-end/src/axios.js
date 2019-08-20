import axios from 'axios'
import store from './store'
import router from './router'

axios.defaults.timeout = 5000 // 超时时间
axios.defaults.baseURL = 'http://127.0.0.1:5000/api' // 发送请求地址

// 添加请求拦截器
axios.interceptors.request.use(
  function (config) {
    // 在发送请求之前做些什么
    const token = window.localStorage.getItem('ackerman-token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  function (error) {
    // 对请求错误做些什么
    return Promise.reject(error)
  }
)

// 添加响应拦截器
axios.interceptors.response.use(
  function (response) {
    // 对响应数据做点什么
    return response
  },
  function (error) {
    // 对响应错误做点什么
    switch (error.response.status) {
      case 401:
        // 跳转到登录页
        if (router.currentRoute.path !== '/login') {
          // 清除 Token 及 已认证 等状态
          store.logoutAction()
          router.replace({
            // TODO: toast提示
            path: '/login',
            query: {
              redirect: router.currentRoute.path
            }
          })
        }
        break
      case 404:
        // TODO: toast提示
        router.back()
        break
    }
    return Promise.reject(error)
  }
)

export default axios