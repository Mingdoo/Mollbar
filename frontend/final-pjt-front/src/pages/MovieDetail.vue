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
    <div class="col-2 mt-5">
      <button @click="changeLike(selectedMovie)" id="changeLikeBtn"></button>
    </div>
    <div class="col-10">
      <div>
        <input type="number" name="" id="userRating" min="1" max="10" required>
        <input type="text" name="" id="userReview">
        <button class="btn btn-primary" @click="updateMovieRating(selectedMovie)">Submit</button>
      </div>
    </div>
    <div v-for="rating in selectedMovie.ratings" :key="rating.id">
      <div class="d-visible" :id="`normalReview${rating.id}`">
        <p>평점 : {{ rating.rate }}</p>
        <p>리뷰 : {{ rating.review }}</p>
        <button class="btn btn-primary" v-if="rating.user === $store.state.userId" @click="editMovieRating(rating)">수정</button>
        <button class="btn btn-warning" v-if="rating.user === $store.state.userId" @click="deleteMovieRating(rating)">삭제</button>
      </div>
      <div class="d-none" :id="`hiddenReview${rating.id}`">
        <input type="number" name="" :id="`updateRating${rating.id}`" min="1" max="10" :value="rating.rate" required>
        <input type="text" name="" :id="`updateReview${rating.id}`" :value="rating.review">
        <button class="btn btn-primary" v-if="rating.user === $store.state.userId" @click="confirmEdittingMovieRating(rating)">확인</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/movies/'
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
  methods: {
    updateMovieRating(movie) {
      const userRating = document.querySelector('#userRating')
      const userReview = document.querySelector('#userReview')
      const token = localStorage.getItem('jwt')
      // console.log(userRating.value)
      axios({
        method: 'post',
        url: `${API_BASE_URL}${movie.id}/ratings/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
        data: {
          rate: userRating.value,
          review: userReview.value
        }
      })
        .then((res) => {
          this.$store.dispatch('updateMovieRating', res.data) 
          userRating.value = ''
          userReview.value = ''
          console.log(this.$store.state.selectedMovie)
        })
    },
    editMovieRating(rating) {
      const normalReview = document.querySelector(`#normalReview${rating.id}`)
      const hiddenReview = document.querySelector(`#hiddenReview${rating.id}`)

      normalReview.classList.remove('d-visible')
      normalReview.classList.add('d-none')

      hiddenReview.classList.remove('d-none')
      hiddenReview.classList.add('d-visible')
      
    },
    confirmEdittingMovieRating(rating) {
      const userRating = document.querySelector(`#updateRating${rating.id}`)
      const userReview = document.querySelector(`#updateReview${rating.id}`)
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_BASE_URL}${this.selectedMovie.id}/ratings/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
        data: {
          rate: userRating.value,
          review: userReview.value
        }
      })
        .then(() => {
          const normalReview = document.querySelector(`#normalReview${rating.id}`)
          const hiddenReview = document.querySelector(`#hiddenReview${rating.id}`)

          rating.review = userReview.value
          rating.rate = userRating.value

          normalReview.classList.add('d-visible')
          normalReview.classList.remove('d-none')

          hiddenReview.classList.add('d-none')
          hiddenReview.classList.remove('d-visible')
        })
    },
    deleteMovieRating(rating) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'delete',
        url: `${API_BASE_URL}${this.selectedMovie.id}/ratings/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
      .then((res) => {
        console.log(res)
        console.log(rating)
        const normalReview = document.querySelector(`#normalReview${rating.id}`)
        normalReview.classList.remove('d-visible')
        normalReview.classList.add('d-none')
      })
    },
    changeLike(movie) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_BASE_URL}${movie.id}/wishlist/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          console.log(res)
          console.log(this.$store.state.selectedMovieLiked)
          const likebtn = document.querySelector('#changeLikeBtn')
          if (likebtn.innerText === 'like') {
            likebtn.innerText = 'dislike'
          } else {
            likebtn.innerText = 'like'
          }
        })
    }
  },
  created(){
    console.log('!!!!')
    console.log(this.$store.state.popularByGenre)
    // const likebtn = document.querySelector('#changeLikeBtn')
    // if (this.$store.state.selectedMovieLiked) {
    //   likebtn.innerText = 'dislike'
    // } else {
    //   likebtn.innerText = 'like'
    // }
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