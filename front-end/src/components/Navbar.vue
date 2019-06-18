<template>
  <v-toolbar
    app
    dark
    color="primary"
  >
    <v-toolbar-side-icon></v-toolbar-side-icon>

    <v-toolbar-title class="white--text">Neko</v-toolbar-title>

    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn
        flat
        to="/"
      >Home</v-btn>
      <v-btn
        flat
        to="/about"
      >About</v-btn>
      <v-btn
        v-if="sharedState.is_authenticated"
        flat
        @click="handleLogout"
      >Logout
        <v-icon right>fas fa-sign-out-alt</v-icon>
      </v-btn>
      <v-btn
        v-else
        flat
        to="/login"
      >Login
        <v-icon right>fas fa-sign-in-alt</v-icon>
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import store from '../store.js'

export default {
  name: 'Navbar',
  data() {
    return {
      sharedState: store.state
    }
  },
  methods: {
    handleLogout() {
      store.logoutAction()
      this.$toasted.success(`你已成功登出!`)
      this.$router.push('/login')
    }
  }
}
</script>