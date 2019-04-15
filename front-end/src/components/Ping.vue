<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'Ping',
    data() {
      return {
        msg: 'Hello, This is Ping.vue component'
      }
    },
    methods: {
      getMessage() {
        const path = 'http://127.0.0.1:5000/api/ping'
        // eslint-disable-next-line
        axios.get(path).then(resolve => this.msg = resolve.data).catch(error => console.error(error))
      }
    },
    created () {
      this.getMessage();
    }
  }
</script>