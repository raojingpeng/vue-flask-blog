<template>
  <v-container
    fluid
    fill-height
  >
    <v-layout
      align-center
      justify-center
    >
      <v-flex
        xs12
        sm8
        md4
      >

        <v-card class="elevation-12">

          <LoginToolbar />

          <v-card-text>
            <v-form
              v-model="valid"
              ref="form"
            >
              <v-text-field
                v-model="username.value"
                :prepend-icon="username.icon"
                :label="username.label"
                :rules="username.rules"
                :loading="loading"
                :disabled="loading"
                required
              >
              </v-text-field>

              <v-text-field
                v-model="password.value"
                :prepend-icon="password.icon"
                :label="password.label"
                :append-icon="password.showPwd ? 'visibility' : 'visibility_off'"
                :rules="password.rules"
                :type="password.showPwd ? 'text' : 'password'"
                :loading="loading"
                :disabled="loading"
                counter
                @click:append="password.showPwd = !password.showPwd"
              ></v-text-field>
            </v-form>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              @click="submit"
              :loading="loading"
              :disabled="!valid"
            >登录</v-btn>
          </v-card-actions>

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import store from '../store'
import LoginToolbar from './LoginToolbar'

export default {
  name: 'Login',
  components: {
    LoginToolbar
  },
  data: () => {
    return {
      loading: false,
      valid: false,
      username: {
        value: '',
        icon: 'person',
        label: '用户名',
        rules: [v => !!v || '请输入用户名']
      },
      password: {
        value: '',
        icon: 'lock',
        label: '密码',
        showPwd: false,
        rules: [v => !!v || '请输入密码', v => v.length >= 8 || '密码不少于8位']
      }
    }
  },
  methods: {
    submit() {
      this.loading = true
      if (this.$refs.form.validate()) {
        const path = '/tokens'
        this.$axios
          .post(
            path,
            {},
            {
              auth: {
                username: this.username.value,
                password: this.password.value
              }
            }
          )
          .then(response => {
            // 客户端记录token
            window.localStorage.setItem('neko-token', response.data.token)
            store.resetNotNewAction()
            store.loginAction()
            // 跳转至首页或重定向
            if (typeof this.$route.query.redirect === 'undefined') {
              this.$router.push('/')
            } else {
              this.$router.push(this.$route.query.redirect)
            }
          })
          .catch(error => {
            if (error.response.status == 401) {
              // 显示错误提示
              this.$toasted.error(`用户名或密码不正确！`, { icon: 'error' })
            } else {
              console.log(error)
            }
            // 取消图标加载状态
            this.loading = false
          })
      }
    },
    click(event) {
      if (this.valid && event.keyCode === 13) {
        this.submit()
      }
    }
  },
  mounted() {
    document.addEventListener('keyup', this.click)
  },
  beforeDestroy() {
    document.removeEventListener('keyup', this.click)
  }
}
</script>