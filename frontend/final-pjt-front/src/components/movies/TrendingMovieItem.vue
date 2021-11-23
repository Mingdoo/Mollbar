<template>
  <div class="carouselbox" @click="movieDetail(trendingMovie)" style="display: inline;">
    <router-link :to="`/movies/${trendingMovie.id}`">
      <img :src="movieUrl" alt="" class="img slider-img">
      <!-- <span class="button heartButton"></span> -->
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'
const BASE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'MovieItem',
  data() {
    return {

    }
  },
  props: {
    trendingMovie: Object
  },
  computed: {
    movieUrl: function() {
      return BASE_URL + this.trendingMovie.poster_path
    }
  },
  methods: {
    movieDetail(selectedMovie){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${selectedMovie.id}`
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('movieDetail', res.data[0])
        this.$router.push({ name: 'MovieDetail' }).catch(() => {})
        // console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}

</script>

<style scoped>

.carouselbox {
  height: 100%;
  width: auto;
  display: inline-block;
  text-align: center;
  padding-bottom: 10px !important;
  display: flex;
  align-items: center;
  position: relative;
}
.carouselbox img {
  height: 80%;
  background-size: contain;
  margin: 30px 20px;
  transition: 0.5s ease;
  /* z-index: 2; */
}
.carouselbox img:hover {
  transform: scale(1.2);
  z-index: 5;
}

/* .heartButton {
  position: relative;
  top: -23%;
  left: -6%;
  z-index: 1;
  text-decoration: none;
} */

/* .carouselbox span:hover {
  transform: scale(2);
  z-index: 6;
} */

</style>