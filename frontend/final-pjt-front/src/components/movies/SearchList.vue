<template>
  <div class="col-md-3">
      <div class="card p-3 mb-2">
          <div class="d-flex justify-content-between">
              <div class="d-flex flex-row align-items-center">
                  <div class="icon"> <i class=""></i> </div>
                  <div class="ms-2 c-details">
                      <h6 class="mb-0"></h6>
                  </div>
              </div>
              <div class="badge"> <span> <b>{{ searchResult.vote_avg }}</b></span> </div>
          </div>
          <div class="mt-5">
            <h3 class="heading" @click="movieDetail(searchResult)">{{ searchResult.title }}<br>
              <router-link :to="`/movies/${searchResult.id}`">
                <img :src="movieUrl" alt="" class="w-100">
              </router-link>
            </h3>
            <div class="mt-5">
                <div class="progress">
                  <div class="progress-bar" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <div class="mt-3"> <span class="text1">32 Applied <span class="text2">of 50 capacity</span></span> </div>
              </div>
          </div>
      </div>
  </div>

</template>

<script>
import axios from 'axios'
const BASE_URL = 'https://image.tmdb.org/t/p/w500/'

export default {
  name: "SearchList",
  props: {
    searchResult: Object
  },
  computed: {
    movieUrl() {
      return BASE_URL + this.searchResult.poster_path
    }
  },
  methods: {
    movieDetail(selectedMovie){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${selectedMovie.id}/`
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('movieDetail', res.data[0])
        this.$router.push({ name: 'MovieDetail' }).catch(() => {})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>
.card {
    border: none;
    border-radius: 10px
}

.c-details span {
    font-weight: 300;
    font-size: 13px
}

.icon {
    width: 50px;
    height: 50px;
    background-color: #eee;
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 39px
}

.badge span {
    background-color: #fffbec;
    width: 60px;
    height: 25px;
    padding-bottom: 3px;
    border-radius: 5px;
    display: flex;
    color: #fed85d;
    justify-content: center;
    align-items: center
}

.progress {
    height: 10px;
    border-radius: 10px
}

.progress div {
    background-color: red
}

.text1 {
    font-size: 14px;
    font-weight: 600
}

.text2 {
    color: #a5aec0
}
</style>