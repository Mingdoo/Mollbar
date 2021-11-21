<template>
  <div class="row mt-5">
    <div class="col-8 media">
      <iframe :src="`https://youtube.com/embed/${selectedMovie.video_url}`" frameborder="0" allow="fullscreen;"></iframe>
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
// const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'MovieDetail',
  data: function() {
    return {
    }
  },
  computed: {
    selectedMovie() {
      return this.$store.state.selectedMovie
    },
  },
  updated(){
  },
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