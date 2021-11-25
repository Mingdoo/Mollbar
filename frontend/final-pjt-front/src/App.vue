<template>
  <div id="app" class="d-flex flex-column h-100 bg-black">
    <main class="flex-shrink-0">
      <nav-bar></nav-bar>
    </main>
    <transition
      name="fade"
      mode="out-in"
    >
      <router-view :key="$route.fullPath"></router-view>
    </transition>
    <foo-ter id="footer"></foo-ter>
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
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap');

#app {
  font-family: 'Noto Sans', sans-serif;
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

.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}

#footer {
  background-color: #EDEDED;
  margin: 0;
  padding: 0;
}
</style>
