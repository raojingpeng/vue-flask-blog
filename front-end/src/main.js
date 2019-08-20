import Vue from 'vue'
import router from './router'
import App from './App.vue'
// 导入 vuetify
import './plugins/vuetify'
// 导入 vue-toasted plugin
import Toasted from 'vue-toasted'
// 导入配置了全局拦截器后的 axios
import axios from './axios'
// 导入 moment.js 用来格式化 UTC 时间为本地时间
import moment from 'moment'
import 'moment/locale/zh-cn'
import VueSweetalert2 from 'vue-sweetalert2'
// 导入 mavon-editor, markdown 样式
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import '@/assets/mavonEditor/github-markdown.min.css'
import '@/assets/mavonEditor/atom-one-light.css'
// 自定义 css 文件
import '@/assets/custom.css'


Vue.config.productionTip = false

Vue.use(mavonEditor)
Vue.use(VueSweetalert2)
Vue.use(Toasted, {
  // 主题样式 primary/outline/bubble
  theme: 'toasted-primary',
  // 显示在页面哪个位置
  position: 'top-right',
  // 显示多久时间（毫秒）
  duration: 3000,
  // 支持哪个图标集合
  iconPack: 'material', // set your iconPack, defaults to material. material|fontawesome|custom-class
  // 可以执行哪些动作
  action: {
    text: 'Cancel',
    onClick: (e, toastObject) => {
      toastObject.goAway(0)
    }
  },
})

Vue.prototype.$axios = axios
Vue.prototype.$moment = moment

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')