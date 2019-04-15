<template>
  <div id="app">
    <navbar></navbar>
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    navbar: Navbar
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
</style>