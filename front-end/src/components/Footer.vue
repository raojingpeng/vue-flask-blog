<template>
  <v-container class="py-1">
    <v-layout
      row
      wrap
    >

      <v-flex
        xs12
        md9
      >
        &copy; Ackerman

        <v-btn
          flat
          icon
          color="grey"
        >
          <v-icon>fas fa-envelope</v-icon>
        </v-btn>

        <v-tooltip top min-width="250px" content-class="wechat" nudge-top="8">
          <template v-slot:activator="{ on }">
            <v-btn
              flat
              icon
              color="green"
              v-on="on"
            >
              <v-icon>fab fa-weixin</v-icon>
            </v-btn>
          </template>
          <v-img :src="require('@/assets/wechat.jpg')"></v-img>
        </v-tooltip>

        <v-tooltip top min-width="250px" content-class="qq" nudge-top="8">
          <template v-slot:activator="{ on }">
            <v-btn
              flat
              icon
              color="blue"
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
          color="red"
        >
          <v-icon>fab fa-weibo</v-icon>
        </v-btn>
         <v-btn
          flat
          icon
        >
          <v-icon>fab fa-github</v-icon>
        </v-btn>

      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'Footer'
}
</script>
