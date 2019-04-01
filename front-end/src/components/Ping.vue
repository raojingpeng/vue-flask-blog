<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
  export default {
    name: 'Ping',
    data() {
      return {
        msg: 'Hello, This is Ping.vue component'
      }
    }
  }
</script>