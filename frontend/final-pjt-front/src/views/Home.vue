<template>
  <div class="home">
    <header class="bg-black py-5">
      <div class="container px-5">
        <div class="row gx-5 align-items-center justify-content-center">
          <div class="col-lg-8 col-xl-7 col-xxl-6">
            <div class="my-5 text-center text-xl-start">
              <h1 class="display-5 fw-bolder text-white mb-2">A Bootstrap 5 template for modern businesses</h1>
              <p class="lead fw-normal text-white-50 mb-4">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Asperiores neque alias sapiente reprehenderit corrupti quam perspiciatis est facere? Quae eligendi culpa vero expedita voluptatem molestias, tenetur fugit accusantium aspernatur non?</p>
              <div class="d-grid gap-3 d-sm-flex justify-content-sm-center justify-content-xl-start">
              </div>
            </div>
          </div>
          <div class="col-xl-5 col-xxl-6 d-none d-xl-block text-center"><img alt="Vue logo" src="../assets/logo.png" class="img-fluid rounded-3 my-5"></div>
        </div>
      </div>
    </header>
    
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
  beforeCreate: function() {
    // axios 요청을 통한 데이터 받아오기.
    this.$store.dispatch('popularByGenre')
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
    }
  }
</script>
