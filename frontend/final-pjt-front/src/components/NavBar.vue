<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info" class="bg-black">
      <router-link to="/" class="navbar-brand mx-5">
        <img src="../../src/assets/logo_transparent.png" alt="" style="width: 50px;">
      </router-link>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="me-auto mb-2 mb-md-0">
          <li class="nav-item" v-if="isLogin"><router-link to="/" class="nav-link" aria-current="page">홈</router-link></li>
          <li class="nav-item" v-if="isLogin"><router-link to="/quiz" class="nav-link">퀴즈</router-link></li>
          <li class="nav-item" v-if="!isLogin"><router-link to="/login" class="nav-link">로그인</router-link></li>
          <li class="nav-item" v-if="!isLogin"><router-link to="/signup" class="nav-link">회원가입</router-link></li>
          <li class="nav-item" v-if="isLogin"><router-link to="/community" class="nav-link">커뮤니티</router-link></li>
          
          
          <b-nav-item-dropdown v-if="isLogin">
            <!-- Using 'button-content' slot -->
            <template #button-content>
              사용자
            </template>
            <b-dropdown-item>
              <router-link to="/profile" class="nav-link text-reset" v-if="isLogin">프로필</router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <a id="logoutlink" class="nav-link text-reset" @click="logOut" style="cursor:pointer;" v-if="isLogin">로그아웃</a>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <div class="d-flex mx-5">
            <input class="form-control me-2" type="search" placeholder="뭐 볼까?" aria-label="Search" v-model="userSearchInput" @keyup.enter="searchMovie">
            <button class="btn btn-outline-secondary w-25" type="submit" @click="searchMovie">검색</button>
          </div>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import axios from 'axios'
const API_SEARCH_URL = 'http://127.0.0.1:8000/api/v1/movies/search/'

export default {
  name: "NavBar",
  data() {
    return {
      userSearchInput: '',
    }
  },
  methods: {
    logOut() {
      localStorage.removeItem('jwt')
      // this.isLogin = false
      this.$store.dispatch('changeLogged')
      this.$router.push({name: 'Login'})
    },
    searchMovie() {
      axios({
        method: 'get',
        url: API_SEARCH_URL,
        params: {
          query: this.userSearchInput,
        }
      })
        .then((res) => {
          this.$store.dispatch('searchMovie', res.data)
        })
        .then(() => {
          this.$router.push({name: "Search"}).catch(() => {})
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    if (localStorage.getItem('jwt')) {
      this.$store.dispatch('changeLogged')
    }
  },
  computed: {
    isLogin() {
      if (localStorage.getItem('jwt')) {
        const token = localStorage.getItem('jwt');
        this.$store.dispatch('setJwtToken', token)
      }
      return this.$store.state.isLogin
    }
  }
}
</script>

<style>

</style>