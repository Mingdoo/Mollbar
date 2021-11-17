<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <movie-list :trending-movie-list="trendingMovieList"></movie-list>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/movies/MovieList'
import axios from 'axios'
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'Home',
  components: {
    MovieList,
  },
  data: function() {
    return {
      trendingMovieList: null,
    }
  },
  created: function() {
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
        // console.log(res)
        this.trendingMovieList = res.data.results
      })
      .catch((err) => {
        console.log(err)
      })
    
    axios({
      method: 'get',
      url: 'https://api.themoviedb.org/3/genre/movie/list',
      params: {
        api_key: API_KEY,
        language: 'ko-KR'
      }
    })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>
