<template>
  <v-container>
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

        <v-tooltip top min-width="250px" id="qqq">
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

      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'Footer'
}
</script>
