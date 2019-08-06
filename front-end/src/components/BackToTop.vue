<template>
  <v-fab-transition>
    <v-btn
      v-show="offset >= 304"
      fixed
      fab
      bottom
      right
      color="transparent"
      @click="$vuetify.goTo(0)"
    >
      <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
  </v-fab-transition>
</template>

<script>
export default {
  name: "BackToTop",
  props: ["offset"]
}
</script>


