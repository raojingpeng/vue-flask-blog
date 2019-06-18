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
                :error-messages="username.error"
                @input="username.error=''"
                required
              >
              </v-text-field>

              <v-text-field
                v-model="email.value"
                :prepend-icon="email.icon"
                :label="email.label"
                :rules="email.rules"
                :loading="loading"
                :disabled="loading"
                :error-messages="email.error"
                @input="email.error=''"
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
                :error-messages="password.error"
                @input="password.error=''"
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
            >立刻注册</v-btn>
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
  name: 'Register',
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
        rules: [v => !!v || '请输入用户名'],
        error: ''
      },
      email: {
        value: '',
        icon: 'email',
        label: '邮箱',
        rules: [
          v => !!v || '请输入邮箱',
          v =>
            /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
              v
            ) || '邮箱格式不正确'
        ],
        error: ''
      },
      password: {
        value: '',
        icon: 'lock',
        label: '密码',
        showPwd: false,
        rules: [
          v => !!v || '请输入密码',
          v => v.length >= 8 || '密码不少于8位'
        ],
        error: ''
      }
    }
  },
  methods: {
    submit() {
      this.loading = true
      if (this.$refs.form.validate()) {
        const path = '/users'
        const payload = {
          username: this.username.value,
          email: this.email.value,
          password: this.password.value
        }
        this.$axios
          .post(path, payload)
          .then(response => {
            store.setNewAction()
            this.$toasted.success('注册成功！请登录', { icon: 'done' })
            this.$router.push('/login')
          })
          .catch(error => {
            console.log(error.response)
            for (var field in error.response.data.message) {
              if (field == 'username') {
                this.username.error = error.response.data.message.username
              } else if (field == 'email') {
                this.email.error = error.response.data.message.email
              } else if (field == 'password') {
                this.password.error = error.response.data.message.password
              }
            }
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