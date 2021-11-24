<template>
  <div class="carouselbox" @click="movieDetail(wishListId)" style="display: inline;">
    <router-link :to="`/movies/${wishListId}`">
      <img :src="movieUrl" alt="" class="img slider-img">
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'
const BASE_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'WistListItem',
  props: {
    wishListId: Number,
  },
  data() {
    return {
      posterPath: '',
    }
  },
  computed: {
    movieUrl() {
      return BASE_URL + this.posterPath
    },
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${this.wishListId}/`
    })
      .then(res => {
        this.posterPath = res.data[0].poster_path
        console.log('ccc')
      })
  },
  methods: {
    movieDetail(wishListId){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/api/v1/movies/${wishListId}/`
      })
      .then((res) => {
        this.$store.dispatch('movieDetail', res.data[0])
        this.$router.push({ name: 'MovieDetail' }).catch(() => {})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style scoped>

</style>