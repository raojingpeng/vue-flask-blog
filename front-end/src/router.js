import Vue from 'vue'
import Router from 'vue-router'
import Ping from '@/components/Ping'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Profile from '@/components/Profile'
import EditProfile from '@/components/EditProfile'

Vue.use(Router)

const router = new Router({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/edit-profile',
      name: 'EditProfile',
      component: EditProfile,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/user/:id',
      name: 'Profile',
      component: Profile,
      meta: {
        requiresAuth: true
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  const token = window.localStorage.getItem('madblog-token')
  //$route.matched 一个数组，包含当前路由的所有嵌套路径片段的路由记录
  if (to.matched.some(record => record.meta.requiresAuth) && (!token || token === null)) {
    next({
      path: '/login',
      query: {redirect: to.fullPath}
    })
  } else if (token && to.path === '/login') {
    next({
      path: from.fullPath
    })
  } else if (to.matched.length === 0) {
    console.log('here')
    Vue.toasted.error('404: NOT FOUND', { icon: 'fingerprint' })
    if (from.name) {
      next({
        name: from.name
      })
    } else {
      next({
        path: '/'
      })
    }
  }
  else {
    next()
  }
})

export default router
