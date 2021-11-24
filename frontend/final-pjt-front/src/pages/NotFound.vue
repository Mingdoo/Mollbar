<template>
  <div id="error-page">
    <div id="description">
      <h1>404 Error</h1>
      <h3>쟈니가 쫓아오기 전에 미로를 탈출하세요.</h3>
    </div>
    <router-link to="/" class="navbar-brand button">
      <b-button variant="secondary">Home</b-button>
    </router-link>
    <router-link to="/movies/694" class="navbar-brand button">
      <b-button variant="secondary" @click="movieDetail">샤이닝(1980) 더 알아보기</b-button>
    </router-link>
    <div></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "NotFound",
  methods: {
    movieDetail() {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/v1/movies/694`
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('movieDetail', res.data[0])
        this.$router.push({ name: 'MovieDetail' }).catch(() => {})
        // console.log(res)
      })
    }
  }
};
</script>

<style scoped>
  #error-page {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    height: 100vh;
    background-size: cover;
    background-image: url(https://www.pngitem.com/pimgs/m/319-3199128_jack-torrance-and-the-maze-in-the-shining.png);
    background-repeat: no-repeat;
    background-position: center;
    padding: 0;
    margin: 0;
    color: darkgary;
    /* overflow: hidden; */
  }

  #description {
    padding-left: 2%;
    /* font-size: 2rem; */
  }

  .button {
    margin: 0;
  }
</style>