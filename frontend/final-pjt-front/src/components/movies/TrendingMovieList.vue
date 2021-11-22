<template>
  <div class="container-carousel">
    <button class="switchLeft sliderButton btn" @click="clickLeft"></button>
    <div class="carousel">
      <trending-movie-item
        v-for="trendingMovie in trendingMovieList"
        :key=trendingMovie.id
        :trending-movie="trendingMovie"
        @movie-detail="movieDetail"
      >
      </trending-movie-item>
    </div>
    <button class="switchRight sliderButton btn" @click="clickRight"></button>
  </div>
</template>

<script>
import TrendingMovieItem from '@/components/movies/TrendingMovieItem'
import $ from 'jquery';

export default {
  name: 'MovieList',
  props: {
    trendingMovieList: Array,
  },
  data() {
    return {
      scrollAmount: 0,
      scrollPerclick: 400
    }
  },
  components: {
    TrendingMovieItem,
  },
  methods: {
    movieDetail(event) {
      console.log(event)
    },
    clickLeft() {
      console.log(this.$el.children[1].clientHeight)
      console.log(this.$el.children[1].clientWidth)
      console.log(this)
      $('.carousel').animate({
          scrollLeft: (this.scrollAmount -= this.scrollPerclick)
        }, 400);
      // this.scrollAmount -= this.scrollPerclick
    },
    clickRight() {
      const sliders = document.querySelector('.carousel')
      console.log(this.$el.clientLeft)
      // this.scrollAmount += this.scrollPerclick
      if (this.scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        $('.carousel').animate({
          scrollLeft: (this.scrollAmount += this.scrollPerclick)
          }, 400);
        }
    },
  }
}
</script>

<style>
.carousel {
  height: 250px;
  width: 85%;
  overflow-y: scroll;
  white-space: nowrap;
  overflow: hidden;
  position: absolute;
  transition: 0.5s ease;
  display: inline-block;
  /* margin-bottom: 10px; */
}
.container-carousel .switchLeft,
.container-carousel .switchRight {
  color: white;
  font-weight: bold;
  text-decoration: none;
  height: 250px;
  width: 25px;
  text-align: center;
  background-color: lightgray;
  font-family: sans-serif;
  top: 0;
  z-index: 3;
}
.sliderButton {
  display: inline-block;
}

.container-carousel .switchLeft{
  position: relative;
  left: -10px;
  top: -100px
}

.container-carousel .switchRight{
  position: relative;
  right: -10px;
  top: -100px
}
</style>