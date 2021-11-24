<template>
  <div class="col-md-6 col-lg-4 col-xl-3 my-5">
    <div class="card p-3 mb-2 bg-dark">
      <div class="d-flex justify-content-between">
        <div class="d-flex flex-row align-items-center">
          <div class="icon">
            <button @click="changeLike(searchResult)" :data-id="searchResult.id"></button>
          </div>
        </div>
        <div class="badge"> <span> <b>{{ searchResult.vote_avg }}</b></span> </div>
      </div>
      <div class="mt-5 row">
        <h6 class="heading text-white np col-12 justify-content-center text-align-center">{{ searchResult.title }}<br>
        </h6>
          <router-link :to="`/movies/${searchResult.id}`">
            <img :src="movieUrl" alt="" class="w-75 cardimage" @click="movieDetail(searchResult)">
          </router-link>
        <div class="mt-5">
          <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
          <div class="mt-3"> <span class="text-white">32 Applied <span class="text2">of 50 capacity</span></span> </div>
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
    },
    // isLiked() {
    //   return this.$store.state.myWishList.includes(this.searchResult.id)
    // }
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
    changeLike(searchResult) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${searchResult.id}/wishlist/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          console.log(res)
          axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/api/v1/accounts/my_wishlist/',
            headers: {
              Authorization: `Bearer ${localStorage.getItem('jwt')}`
            }
          })
          .then((res) => {
            this.$store.dispatch('myWishList', res.data)
          })
          .then(res => {
            const btnId = searchResult.id
            console.log('asdfasdfd', btnId)
            const likebtn = document.querySelector(`[id=${CSS.escape(btnId)}]`)
            if (likebtn.classList.contains('far')) {
              likebtn.classList.remove('far')
              likebtn.classList.add('fas')
            } else {
              likebtn.classList.remove('fas')
              likebtn.classList.add('far')
            }
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
        })
    }
  },
  mounted() {
    const btnId = this.searchResult.id
    const likebtn = document.querySelector(`[data-id=${CSS.escape(btnId)}]`)
    // console.log(likebtn)
    // console.log(this.$store.state.myWishList.includes(this.searchResult.id))
    if (this.$store.state.myWishList.includes(this.searchResult.id)) {
      likebtn.innerHTML = `<i class="fas fa-star" id="${btnId}"></i>`
      } else {
      likebtn.innerHTML = `<i class="far fa-star" id="${btnId}"></i>`
    }
  }
}
</script>

<style>
.card {
    border: none;
    border-radius: 10px;
    height: 100%;
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
    background-color: #2c2b27;
    width: 60px;
    height: 30px;
    padding-bottom: 3px;
    border-radius: 5px;
    display: flex;
    color: crimson;
    justify-content: center;
    align-items: center;
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

.cardimage {
  background-size: contain;
  margin: 30px 20px;
  transition: 0.5s ease;
  /* z-index: 2; */
}

.cardimage:hover {
  transform: scale(1.5);
  z-index: 5;
}

.icon button {
  background: transparent;
  border: none;
}

.fa-star {
  color: #ff0000;
  background: none;
  border: none;
  font-size: 2rem;
}
</style>