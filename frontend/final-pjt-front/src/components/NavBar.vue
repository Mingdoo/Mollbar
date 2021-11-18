<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">(로고)</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item" v-if="isLogin">
            <router-link to="/" class="nav-link" aria-current="page">(로고)</router-link>
          </li>
          <li class="nav-item" v-if="isLogin">
            <router-link to="/profile" class="nav-link">(프로필)</router-link>
          </li>
          <li class="nav-item" v-if="!isLogin">
            <router-link to="/login" class="nav-link">(로그인)</router-link>
          </li>
          <li class="nav-item" v-if="!isLogin">
            <router-link to="/signup" class="nav-link">(회원가입)</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/v404v" class="nav-link disabled">(404)</router-link>
          </li>
          <li class="nav-item" v-if="isLogin">
            <a id="logoutlink" class="nav-link" @click="logOut" style="cursor:pointer;">(로그아웃)</a>
          </li>
        </ul>
        <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      // isLogin: this.$store.state.isLogin
    }
  },
  methods: {
    logOut() {
      localStorage.removeItem('jwt')
      // this.isLogin = false
      this.$store.dispatch('changeLogged')
      this.$router.push({name: 'Login'})
    }
  },
  created() {
    if (localStorage.getItem('jwt')) {
      this.$store.dispatch('changeLogged')
    }
  },
  computed: {
    isLogin() {
      return this.$store.state.isLogin
    }
  }
}
</script>

<style>

</style>