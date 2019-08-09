<template>
  <footer class="container py-1">
    <v-layout row justify-space-between style="align-items: center">

      <span>&copy; Ackerman</span>
      <span>
        <v-btn
          flat
          icon
          href="https://github.com/raojingpeng"
        >
          <v-icon>fab fa-github</v-icon>
        </v-btn>

        <v-tooltip
          top
          min-width="250px"
          content-class="wechat"
          nudge-top="5"
        >
          <template v-slot:activator="{ on }">
            <v-btn
              flat
              icon
              color="green lighten-1"
              v-on="on"
            >
              <v-icon>fab fa-weixin</v-icon>
            </v-btn>
          </template>
          <v-img :src="require('@/assets/wechat.jpg')"></v-img>
        </v-tooltip>

        <v-tooltip
          top
          min-width="250px"
          content-class="qq"
          nudge-top="5"
        >
          <template v-slot:activator="{ on }">
            <v-btn
              flat
              icon
              color="light-blue lighten-1"
              v-on="on"
            >
              <v-icon>fab fa-qq</v-icon>
            </v-btn>
          </template>
          <v-img :src="require('@/assets/qq.jpg')"></v-img>
        </v-tooltip>

        <v-btn
          flat
          icon
          color="grey lighten-1"
          href="mailto:withrjp@gmail.com"
        >
          <v-icon>fas fa-envelope</v-icon>
        </v-btn>

        <v-btn
          flat
          icon
          color="red lighten-1"
          href="https://weibo.com/u/3045616841"
        >
          <v-icon>fab fa-weibo</v-icon>
        </v-btn>
      </span>

</v-layout>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>
