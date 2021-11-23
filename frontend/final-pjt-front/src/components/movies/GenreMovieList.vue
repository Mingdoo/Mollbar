<template>
  <div>
    <div>
      <h2>
        {{ this.genreName[this.genre] }} 영화는 어때요?
      </h2>
    </div>
    <div class="container-carousel row">
      <div class="col-1">
        <button class="switchLeft sliderButton btn" @click="clickLeft">&lt;</button>
      </div>
      <div class="col-10">
        <div :id="`carousel${this.genre}`" v-if="this.movieList.length > 0">
          <genre-movie-item
            v-for="movieByGenre in movieList"
            :key="movieByGenre.id"
            :movie-by-genre="movieByGenre"
          >
          </genre-movie-item>
        </div>
      </div>
      <div class="col-1">
        <button class="switchRight sliderButton btn" @click="clickRight">&gt;</button>
      </div>
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
      movieList: [],
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
  methods: {
    clickLeft() {
      $(`#carousel${this.genre}`).animate({
          scrollLeft: (this.scrollAmount -= this.scrollPerclick)
        }, 400);
      this.scrollAmount -= this.scrollPerclick
    },
    clickRight() {
      const sliders = document.querySelector(`#carousel${this.genre}`)
      this.scrollAmount += this.scrollPerclick
      if (this.scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        $(`#carousel${this.genre}`).animate({
          scrollLeft: (this.scrollAmount += this.scrollPerclick)
          }, 400);
        }
    },
  },
  // computed: {
  //   movieList() {
  //     return _.shuffle(this.$store.state.popularByGenre[this.genre])
  //   }
  // },
  mounted() {
    setTimeout(() => {
      this.movieList = _.shuffle(this.$store.state.popularByGenre[this.genre])
    }, 1500)
  }
}
</script>

<style>
[id^="carousel"] {
  height: 300px;
  width: 100%;
  overflow-y: scroll;
  white-space: nowrap;
  overflow: hidden;
  position: relative;
  transition: 0.5s ease;
  display: inline-block;
  /* margin-bottom: 10px; */
}

.sliderButton {
  display: inline-block;
}
</style>