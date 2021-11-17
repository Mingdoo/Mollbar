<template>
  <div>
    <movie-item
      v-for="trendingMovie in trendingMovieList"
      :key=trendingMovie.id
      :trending-movie="trendingMovie"
      @movie-detail="movieDetail"
    >
    </movie-item>
  </div>
</template>

<script>
import MovieItem from '@/components/movies/MovieItem'

export default {
  name: 'MovieList',
  props: {
    trendingMovieList: Array
  },
  components: {
    MovieItem,
  },
  methods: {
    movieDetail(event) {
      console.log(event)
      // this.$emit('movieDetail')
    }
  }
}
</script>

<style>

</style>