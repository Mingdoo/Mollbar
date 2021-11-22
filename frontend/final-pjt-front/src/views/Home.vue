<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <trending-movie-list></trending-movie-list>
    <genre-movie-list v-for="genre in genres" :key="genre" :genre="genre"></genre-movie-list>
  </div>
</template>

<script>
// @ is an alias to /src
import TrendingMovieList from '@/components/movies/TrendingMovieList'
import GenreMovieList from '@/components/movies/GenreMovieList';
import axios from 'axios'
const API_KEY = process.env.VUE_APP_API_KEY
const genres = [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770]

export default {
  name: 'Home',
  components: {
    TrendingMovieList,
    GenreMovieList,
  },
  data: function() {
    return {
      trendingMovieList: null,
      genres,
    }
  },
  mounted: function() {
    // axios 요청을 통한 데이터 받아오기.
    axios({
      method: 'get',
      url: 'https://api.themoviedb.org/3/trending/movie/week',
      params: {
        api_key: API_KEY,
        language: 'ko-KR'
      }
    })
    .then((res) => {
      this.$store.state.trendingMovieList = res.data.results
    })
    .catch((err) => {
      console.log(err)
    })

    genres.forEach((genre) => {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/genre-popular/${genre}/`,
      })
        .then((res) => {
          this.$store.state.popularByGenre[genre] = res.data
          this.$store.dispatch('popularByGenre', {
            genre: genre,
            data: res.data
          })
        })
        .catch((err) => {
          console.log(err)
        })
      })
    }
  }
</script>
