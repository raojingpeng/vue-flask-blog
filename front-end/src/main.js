import Vue from 'vue'
import VueToasted from 'vue-toasted'
import App from './App.vue'
import router from './router'
import './assets/iconfonts/material-icons.css'
import 'bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false

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

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')