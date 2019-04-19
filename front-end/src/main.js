import Vue from 'vue'
import VueToasted from 'vue-toasted'
import moment from 'moment'
import App from './App.vue'
import router from './router'
import axios from './axios'
import './assets/iconfonts/material-icons.css'
import 'bootstrap/dist/css/bootstrap.css'
//自定义 css 文件
import './assets/core.css'
import './assets/custom.css'

Vue.use(VueToasted, {
  theme: 'bubble',
  position: 'top-right',
  duration: 3000,
  iconPack: 'material',
  action: {
    text: 'Cancel',
    onClick: (e, toastObject) => {
      toastObject.goAway(0)
    }
  },
});

Vue.config.productionTip = false
Vue.prototype.$moment = moment
Vue.prototype.$axios = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')