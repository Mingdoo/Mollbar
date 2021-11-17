<template>
  <div @click="movieDetail" @mouseenter="sizeUp" @mouseleave="sizeDown">
    <h1>{{ trendingMovie.title }}</h1>
    <!-- <h3>{{ trendingMovie.overview }}</h3> -->
    <img :src="movieUrl" alt="" class='img' :class="{ 'cursuron': cursuron }">
  </div>
</template>

<script>
const BASE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'MovieItem',
  data() {
    return {
      cursuron: false
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
    movieDetail(){
      this.$store.dispatch('movieDetail', this.trendingMovie)
      this.$router.push({ name: 'MovieDetail' })
    },
    sizeUp(){
      this.cursuron = true
    },
    sizeDown(){
      this.cursuron = false
    }
  }
}
</script>

<style scoped>
.img {
  width: 20%;
}
.cursuron {
  width: 30%;
}
</style>