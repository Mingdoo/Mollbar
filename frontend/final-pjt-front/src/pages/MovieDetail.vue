<template>
  <div class="row">
    <div class="col-8 media">
      <iframe :src="selectedMovieUrl" frameborder="0" allow="fullscreen;"></iframe>
    </div>
    <div class="col-4 np">
      <h1>
        {{ selectedMovie.title }}
      </h1>
      <hr>
      <h5>
        {{ selectedMovie.overview }}
      </h5>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'MovieDetail',
  data: function() {
    return {
      selectedMovie: this.$store.state.selectedMovie,
      selectedMovieUrl: '',
    }
  },
  updated(){
  },
  mounted() {
    if (this.$store.state.selectedMovie){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.$store.state.selectedMovie.id}/videos`,
        params: {
          api_key: API_KEY
        }
      })
        .then((res) => {
          console.log(res)
          this.selectedMovieUrl = `https://www.youtube.com/embed/${res.data.results[0].key}`
        })
    }
  }
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/nanumpenscript.css);
.np {
  font-family: 'Nanum Pen Script',
  cursive;
}
.h2 {
  justify-content: center;
  align-content: center;
}
.media {
  position: relative;
  padding-bottom: 37.5%;
  height: 0;
  overflow: hidden;
  margin-top: 20px;
}
.media iframe {
    position: absolute;
    top: 10; 
    left: 0;
    width: 100%;
    height: 100%;
}
</style>