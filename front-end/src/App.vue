<template>
  <v-app>
    <Navbar />

    <v-content v-scroll="onScroll">
      <router-view />
    </v-content>

    <BackToTop :offset="offset" />

    <v-divider></v-divider>
    
    <Footer></Footer>
  </v-app>
</template>

<script>
export default {
  name: "App",
  components: {
    Navbar: () => import("@/components/Navbar"),
    BackToTop: () => import("@/components/BackToTop"),
    Footer: () => import("@/components/Footer")
  },
  data: () => ({ offset: 0 }),
  methods: {
    onScroll(e) {
      this.offset = e.target.documentElement.scrollTop
    }
  }
}
</script>