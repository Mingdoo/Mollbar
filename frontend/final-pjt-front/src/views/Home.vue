<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <trending-movie-list
    :trending-movie-list="trendingMovieList"
    >
    </trending-movie-list>
  </div>
</template>

<script>
// @ is an alias to /src
import TrendingMovieList from '@/components/movies/TrendingMovieList'
import axios from 'axios'
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'Home',
  components: {
    TrendingMovieList,
  },
  data: function() {
    return {
      trendingMovieList: null
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
        this.$store.state.trendingMovieList = res.data.results
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>
