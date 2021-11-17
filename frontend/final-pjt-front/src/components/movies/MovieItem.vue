<template>
  <div>
    <h1>{{ trendingMovie.title }}</h1>
    <!-- <h3>{{ trendingMovie.overview }}</h3> -->
    <img :src="movieUrl" alt="">
  </div>
</template>

<script>
const BASE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'MovieItem',
  props: {
    trendingMovie: Object
  },
  computed: {
    movieUrl: function() {
      return BASE_URL + this.trendingMovie.poster_path
    }
  }
}
</script>

<style>

</style>