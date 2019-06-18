<template>
  <v-toolbar
    dark
    color="primary"
  >

    <v-toolbar-items :style="{left: '50%'}">
      <v-btn
        flat
        large
        to="/login"
        absolute
        :style="{left: '50%', transform: 'translateX(-100%)'}"
      >登录</v-btn>
      <v-btn
        flat
        large
        to="/register"
        absolute
        :style="{left: '50%'}"
      >注册</v-btn>
    </v-toolbar-items>

  </v-toolbar>
</template>

<script>
export default {
  name: 'LoginToolbar'
}
</script>