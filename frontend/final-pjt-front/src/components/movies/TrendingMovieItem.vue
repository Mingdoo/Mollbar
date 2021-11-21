<template>
  <div class="carouselbox" @click="movieDetail(trendingMovie)" style="display: inline;">
    <router-link :to="`/movies/${trendingMovie.id}`">
      <img :src="movieUrl" alt="" class="img slider-img">
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
        this.$store.dispatch('movieDetail', res.data)
        this.$router.push({ name: 'MovieDetail' })
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
  height: 10%;
  width: auto;
  display: inline-block;
  text-align: center;
  padding-bottom: 10px !important;
  display: flex;
  align-items: center;
}
.carouselbox img {
  height: 75%;
  background-size: cover;
  margin: 0px 20px;
  cursor: pointer;
  transition: 0.5s ease;
  z-index: 2;
  margin-top: 6%;
}
.carouselbox img:hover {
  transform: scale(1.3);
  z-index: 5;
}
</style>