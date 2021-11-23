<template>
  <div class="container">
    <div class="row mt-5">
      
      <div v-if="selectedMovie.video_url" class="col-6 media">
        <iframe :src="`https://youtube.com/embed/${selectedMovie.video_url}`" frameborder="0" allow="fullscreen;"></iframe>
      </div>
      <!-- video url이 없는 경우 -->
      <div v-else class="col-4 offset-1 media">
        <img :src="`https://image.tmdb.org/t/p/w500/${selectedMovie.poster_path}`" alt="">
      </div>

      <div v-if="selectedMovie.video_url" :selectedMovie="selectedMovie" class="col-5 offset-1 np">
        <!-- 필요한 정보 : 제목 / 줄거리 / 배우 / 개봉 날짜 / 점수 -->
        <h1 class="vertical-line bold">
          {{ selectedMovie.title }}
        </h1>
        <hr>
        
        <div class="row d-flex align-items-center">
          <!-- 유저 평가 점수 (%로 표시) -->
          <div class="col-11">
            <!-- TODO: color-flow=true 적용할 지 결정하기 -->
            <k-progress 
              color=#ff0000
              type="line"
              line-height=8
              :percent="userPercentage"
              style="margin: 0 0 0 16px;"
            >
            </k-progress>
          </div>
          <div class="col-1">
            <!-- <img src="" alt="" @click="changeLike(selectedMovie)" id="changeLikeBtn" />
            <i class="far fa-star"></i> -->
            <button @click="changeLike(selectedMovie)" id="changeLikeBtn"></button>
          </div>
        </div>
        <p class="align-left mt-2">
          <span class="bold h5">개봉일 </span>
          <span>{{ selectedMovie.released_date }}</span>
        </p>
        <p class="align-left">
          <span class="bold h5">출연</span>
          <span v-for="actor in selectedMovie.actors" :key="actor">
            {{ actor }} | 
          </span>
        </p>
        <hr>
        <p class="overview align-left">
          {{ selectedMovie.overview }}
        </p>
      </div>
      <!-- video url이 없는 경우 -->
      <div v-else class="col-5 offset-1 np">  
        <h1 class="vertical-line bold">
          {{ selectedMovie.title }}
        </h1>
        <hr>
        
        <div class="row d-flex align-items-center">
          <div class="col-11">
            <k-progress 
              color=#ff0000
              type="line"
              line-height=8
              :percent="userPercentage"
              style="margin: 0 0 0 16px;"
            >
            </k-progress>
          </div>
          <div class="col-1">
            <i class="far fa-star"></i> -->
            <button @click="changeLike(selectedMovie)" id="changeLikeBtn"></button>
          </div>
        </div>
        <p class="align-left mt-2">
          <span class="bold h5">개봉일 </span>
          <span>{{ selectedMovie.released_date }}</span>
        </p>
        <p class="align-left">
          <span class="bold h5">출연</span>
          <span v-for="actor in selectedMovie.actors" :key="actor">
            {{ actor }} | 
          </span>
        </p>
        <hr>
        <p class="overview align-left">
          {{ selectedMovie.overview }}
        </p>
      </div>

      <!-- <div class="col-2 mt-5">
        <button @click="changeLike(selectedMovie)" id="changeLikeBtn"></button>
      </div> -->
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
  </div>
</template>

<script>
import axios from 'axios'
import KProgress from 'k-progress';
// import StarRating from 'vue-star-rating'

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/movies/'
// const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'MovieDetail',
  data: function() {
    return {
      rate: 0,
    }
  },
  components: {
    KProgress,
    // StarRating
  },
  computed: {
    selectedMovie() {
      return this.$store.state.selectedMovie
    },
    userPercentage() {
      return parseInt(this.selectedMovie.vote_avg * 10)
    }
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
          .catch((err) => {
            console.log(err)
          })
          const likebtn = document.querySelector('#changeLikeBtn')
          if (likebtn.innerHTML === '<i class="fas fa-star"></i>') {
            likebtn.innerHTML = '<i class="far fa-star"></i>'
          } else {
            likebtn.innerHTML = '<i class="fas fa-star"></i>'
          }
          console.log(res)
        })
    }
  },
  mounted(){
    const likebtn = document.querySelector('#changeLikeBtn')
    console.log(likebtn)
    console.log(this.$store.state.myWishList.includes(this.selectedMovie.id))
    if (this.$store.state.myWishList.includes(this.selectedMovie.id)) {
      likebtn.innerHTML = '<i class="fas fa-star"></i>'
      } else {
      likebtn.innerHTML = '<i class="far fa-star"></i>'
    }
  },
}
</script>

<style>
/* @import url(//fonts.googleapis.com/earlyaccess/nanumpenscript.css); */
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);

.vertical-line {
  /* border-left: 3px solid #ff0000; */
  border-left: 3px solid #ff0000;
}
.np {
  font-family: 'Noto Sans KR', sans-serif;
  color: #444444;
}
.h5 {
  font-size: 1.5rem;
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

.bold {
  font-weight: bold;
}

.align-left {
  text-align: left;
  padding-left: 1rem;
}

.overview {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 10;        /* 최대 10줄까지만 보여주기 */
  -webkit-box-orient: vertical;
}

#changeLikeBtn {
  background: none;
  border: none;
  color: #ff0000;
  font-size: 1.5rem;
  padding: 0;
  margin: 0;
  transform: translate(-10px, -3px);
}

#changeLikeBtn:hover {
  transform: scale(1.2) translate(-8px, -3px);
}
</style>