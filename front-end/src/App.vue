<template>
  <v-app>
    <Navbar />
    <v-content v-scroll="onScroll">
      <router-view />
    </v-content>

    <v-fab-transition>
      <v-btn
        v-show="offsetTop >= 304"
        dark
        fixed
        fab
        bottom
        right
        color="red"
        @click="$vuetify.goTo(0, {duration: 300, offset: 0, easing: 'easeInOutCubic'})"
      >
        <v-icon>keyboard_arrow_up</v-icon>
      </v-btn>
    </v-fab-transition>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar
  },
  data() {
    return {
      offsetTop: 0
    }
  },
  methods: {
    onScroll(e) {
      this.offsetTop = e.target.documentElement.scrollTop
    }
  }
}
</script>