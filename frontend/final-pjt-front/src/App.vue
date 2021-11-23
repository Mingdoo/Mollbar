<template>
  <div id="app" class="d-flex flex-column h-100 bg-black">
    <main class="flex-shrink-0">
      <nav-bar></nav-bar>
    </main>
    <div class="">
      <router-view :key="$route.fullPath"></router-view>
    </div>
    <foo-ter></foo-ter>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar';
import FooTer from '@/components/Footer';

export default {
  name: "App",
  components: {
    NavBar,
    FooTer,
  },
  // data() {
  //   return {
  //   }
  // },
  // created() {
  //   const token = localStorage.getItem('jwt')
  //   if (token) {
  //     thi
  //   }
  // },
  // updated() {
  //   const token = localStorage.getItem('jwt')
  //   if (token) {
  //     this.isLogin = true
  //   }
  // }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* background-color: aquamarine; */
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
