<template>
  <div>
    <el-button round>{{ msg }}</el-button>
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
        axios.get(path).then(resolve => this.msg = resolve.data).catch(error => console.error(error))
      }
    },
    created () {
      this.getMessage();
    }
  }
</script>