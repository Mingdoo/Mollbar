<template>
  <div class="container-carousel row">
    <div class="col-1">
      <button class="switchLeft sliderButton btn" @click="clickLeft"></button>
    </div>
    <div class="carousel col-10">
      <trending-movie-item
        v-for="trendingMovie in trendingMovieList"
        :key="trendingMovie.id"
        :trending-movie="trendingMovie"
      >
      </trending-movie-item>
    </div>
    <div class="col-1">
      <button class="switchRight sliderButton btn" @click="clickRight"></button>
    </div>
  </div>
</template>

<script>
import TrendingMovieItem from '@/components/movies/TrendingMovieItem'
import $ from 'jquery';

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
  color: white;
  font-weight: bold;
  text-decoration: none;
  height: 200px;
  width: 25px;
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