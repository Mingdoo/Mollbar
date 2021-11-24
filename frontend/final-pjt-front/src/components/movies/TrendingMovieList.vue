<template>
  <div class="container-carousel row">
    <h2 class="np text-white" style="cursor:pointer;" @click="searchMovie">
      이번주 박스오피스 영화는 어때요?
    </h2>
    <div class="col-1" @click="clickLeft" style="cursor:pointer;">
      <i class="fa fa-chevron-left" aria-hidden="true" style="font-size: 40px;"></i>
    </div>
    <div class="carousel col-10">
      <trending-movie-item
        v-for="trendingMovie in trendingMovieList"
        :key="trendingMovie.id"
        :trending-movie="trendingMovie"
      >
      </trending-movie-item>
    </div>
    <div class="col-1" @click="clickRight" style="cursor:pointer;">
      <i class="fa fa-chevron-right" aria-hidden="true" style="font-size: 40px;"></i>
    </div>
  </div>
</template>

<script>
import TrendingMovieItem from '@/components/movies/TrendingMovieItem'
import $ from 'jquery';
import axios from 'axios';
const API_SEARCH_URL = 'http://127.0.0.1:8000/api/v1/movies/search/'


export default {
  name: 'MovieList',
  data() {
    return {
      scrollAmount: 0,
      scrollPerclick: 200
    }
  },
  components: {
    TrendingMovieItem,
  },
  methods: {
    clickLeft() {
      $('.carousel').animate({
          scrollLeft: (this.scrollAmount -= this.scrollPerclick)
        }, 400);
      this.scrollAmount -= this.scrollPerclick
    },
    clickRight() {
      const sliders = document.querySelector('.carousel')
      console.log(this.$el.clientLeft)
      this.scrollAmount += this.scrollPerclick
      if (this.scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        $('.carousel').animate({
          scrollLeft: (this.scrollAmount += this.scrollPerclick)
          }, 400);
        }
    },
    searchMovie() {
      axios({
        method: 'get',
        url: API_SEARCH_URL,
        params: {
        }
      })
        .then((res) => {
          this.$store.dispatch('searchMovie', res.data)
        })
        .then(() => {
          this.$router.push({name: "Search"})
          setTimeout(() => {
            $('html, body').animate({
              scrollTop : 0
            }, 400);
          }, 500)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  computed: {
    trendingMovieList() {
      return this.$store.state.trendingMovieList
    }
  }
}
</script>

<style>
.container-carousel {
  text-align: center;
  align-items: center;
}

.carousel {
  height: 300px;
  width: 100%;
  overflow-y: scroll;
  white-space: nowrap;
  overflow: hidden;
  position: absolute;
  transition: 0.5s ease;
  display: inline-block;
  /* overflow: -moz-hidden-unscrollable; */
}

.container-carousel .switchLeft,
.container-carousel .switchRight {
  color: rgb(255, 255, 255);
  font-weight: bold;
  text-decoration: none;
  height: 300px;
  width: 40px;
  font-size: 30px;
  text-align: center;
  background-color: lightgray;
  font-family: sans-serif;
  z-index: 3;
  position: relative;
}
.sliderButton {
  display: inline-block;
}

.container-carousel .switchLeft{
  position: relative;
  left: -10px;
}

.container-carousel .switchRight{
  position: relative;
  right: -10px;
}
</style>