<template>
  <div class="home">
    <header class="bg-black py-5">
      <div class="container px-5">
        <div class="row gx-5 align-items-center justify-content-center">
          <div class="col-xl-5 col-xxl-6 d-none d-xl-block text-center"><img alt="Vue logo" src="../assets/logo_transparent.png" class="img-fluid rounded-3 my-5"></div>
          <div class="col-lg-8 col-xl-7 col-xxl-6">
            <div class="my-5 text-center text-xl-start">
              <h1 class="display-5 fw-bolder text-white mb-2 hometitle">우리.. 영화볼래요?</h1>
              <p class="lead fw-normal text-white-50 mb-4">영화는 많고 뭘 봐야할지 모르겠다면, <b class="h4">몰봐</b>로 오세요! 재미있고 즐거운 영화 정보가 가득! 장르별 영화, 검색은 기본! 재미는 2배 기쁨은 5배!</p>
              <div class="d-grid gap-3 d-sm-flex justify-content-sm-center justify-content-xl-start">
              </div>
            </div>
          </div>
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
import _ from 'lodash'
const API_KEY = process.env.VUE_APP_API_KEY
const genres = _.shuffle([12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770])

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

<style>
.hometitle:after {
  content: "   ❤";
  visibility: hidden;
  transition: visibility 0s linear 0.5s, opacity 0.5s linear, font 0.05s linear;
  color: red;
  font-size: 0;
}

.hometitle:hover:after {
  visibility: visible;
  font-size: 30px;
}
</style>