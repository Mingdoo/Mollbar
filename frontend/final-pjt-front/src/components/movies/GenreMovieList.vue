<template>
  <div>
    <div>
      <h2>
        {{ this.genreName[this.genre] }} 영화는 어때요?
      </h2>
    </div>
    <div class="container-carousel">
      <button class="switchLeft sliderButton btn" @click="clickLeft"></button>
      <div :id="`carousel${this.genre}`">
        <genre-movie-item
          v-for="movieByGenre in MovieList"
          :key="movieByGenre.id"
          :movie-by-genre="movieByGenre"
        >
        </genre-movie-item>
      </div>
      <button class="switchRight sliderButton btn" @click="clickRight"></button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import GenreMovieItem from '@/components/movies/GenreMovieItem';
import $ from 'jquery';



export default {
  name: "GenreMovieList",
  props: {
    genre: Number,
  },
  data() {
    return {
      scrollAmount: 0,
      scrollPerclick: 200,
      genreName : {
        '12' : '어드벤쳐',
        '14' : '판타지',
        '16' : '애니메이션',
        '18' : '드라마',
        '27' : '호러',
        '28' : '액션',
        '35' : '코미디',
        '36' : '역사',
        '37' : '서부',
        '53' : '스릴러',
        '80' : '범죄',
        '99' : '다큐멘터리',
        '878' : 'SF',
        '9648' : '미스터리',
        '10402' : '음악',
        '10749' : '로맨스',
        '10751' : '가족',
        '10752' : '전쟁',
        '10770' : 'TV 영화',
      }
    }
  },
  components: {
    GenreMovieItem
  },
  computed: {
    MovieList() {
      return _.shuffle(this.$store.state.popularByGenre[this.genre])
    }
  },
  methods: {
    clickLeft() {
      console.log($(`#carousel${this.genre}`))
      $(`#carousel${this.genre}`).animate({
          scrollLeft: (this.scrollAmount -= this.scrollPerclick)
        }, 400);
      this.scrollAmount -= this.scrollPerclick
    },
    clickRight() {
      console.log(this.genre)
      const sliders = document.querySelector(`#carousel${this.genre}`)
      this.scrollAmount += this.scrollPerclick
      if (this.scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        $(`#carousel${this.genre}`).animate({
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
[id^="carousel"] {
  height: 250px;
  width: 85%;
  overflow-y: scroll;
  white-space: nowrap;
  overflow: hidden;
  position: relative;
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