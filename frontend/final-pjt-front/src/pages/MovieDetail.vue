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

      <div v-if="selectedMovie.video_url" :selectedMovie="selectedMovie" class="col-5 offset-1 np pb-4">
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
              :color-flow="true"
              type="line"
              :line-height="8"
              :percent="userPercentage"
              style="margin: 0 0 0 16px;"
            >
            </k-progress>
          </div>
          <div class="col-1">
            <button @click="changeLike(selectedMovie)" id="changeLikeBtn"></button>
          </div>
        </div>
        <div class="align-left mt-3 mb-3 row">
          <div class="col-2">
            <span class="bold h5">개봉일 </span>
          </div>
          <div class="col-10">
            <span>{{ selectedMovie.released_date }}</span>
          </div>
        </div>
        <div class="align-left row">
          <div class="col-2">
            <span class="bold h5">출연</span>
          </div>
          <div class="col-10">
            <span v-for="actor in selectedMovie.actors" :key="actor">
              {{ actor }} | 
            </span>
          </div>
        </div>
        <hr>
        <p class="overview align-left">
          {{ selectedMovie.overview }}
        </p>
      </div>
      <!-- video url이 없는 경우 -->
      <div v-else class="col-5 offset-1 np pb-4">  
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
            <button @click="changeLike(selectedMovie)" id="changeLikeBtn"></button>
          </div>
        </div>
        <p class="align-left mt-2">
          <span class="bold h5">개봉일 </span>
          <span>{{ selectedMovie.released_date }}</span>
        </p>
        <div class="align-left row d-flex">
          <div class="bold h5 col-2">
            <span>출연 </span>
          </div>
          <div class="col-10">
            <span v-for="actor in selectedMovie.actors" :key="actor">
              {{ actor }} | 
            </span>
          </div>
        </div>
        <hr>
        <p class="overview align-left">
          {{ selectedMovie.overview }}
        </p>
      </div>

      <br><hr><br>

      <!-- 평가 입력창 -->
      <div class="row">
        <star-rating class="col-3"
          :increment="0.5"
          :glow="3"
          :clearable=true
          :show-rating="false"
          :star-size="40"
          @rating-selected="setRating"
          v-model="starRating"  
        >
        </star-rating>
        <!-- <input type="number" name="" id="userRating" :starRating="starRating" min="1" max="10" required> -->
        <input type="text" class="col-7" id="userReview" v-model="reviewComment" @keyup.enter="updateMovieRating(selectMovie)">
        <button 
          class="btn btn-outline-success col-1 offset-1 white"
          style="font-size: 18px;"
          @click="updateMovieRating(selectedMovie)"
          v-if="this.starRating && this.reviewComment"
        >
          등록
        </button>
      </div>

      <!-- 평가 목록 -->
      <table class="table table-borderless mt-4">
        <tbody>
          <tr v-for="rating in selectedMovie.ratings" :key="rating.id" style="overflow: hidden; vertical-align: middle;">
            <td style="margin-left: 0;" class="white">
              <!-- TODO: 해당 유저의 프로필로 이동하기 -->
              {{rating.username}}
            </td>
            <td>
              <star-rating
                :increment="0.5"
                :star-size="24"
                :rating="rating.rate / 2"
                :show-rating="false"
                :read-only="true"
                color="#ff0000"
              >
              </star-rating>  
            </td>
            <td colspan="4" class="d-flex justify-content-between">
              <div style="max-width: 85%; transform: translateY(6%)" class="white">{{rating.review}}</div>
              <div v-if="rating.user === $store.state.userId" class="np">
                <button class="btn pt-0 pb-0 mt-0 mb-0" style="color: #ff0000; font-size: 18px;" @click="deleteMovieRating(rating)">
                  <i class="far fa-trash-alt h5 mb-0"></i>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="d-none" v-for="rating in selectedMovie.ratings" :key="rating.id" :id="`hiddenReview${rating.id}`">
        <input type="number" name="" :id="`updateRating${rating.id}`" min="1" max="10" :value="rating.rate" required>
        <input type="text" name="" :id="`updateReview${rating.id}`" :value="rating.review">
        <button class="btn" v-if="rating.user === $store.state.userId" @click="confirmEdittingMovieRating(rating)">확인</button>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import KProgress from 'k-progress';
import StarRating from 'vue-star-rating'

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/movies/'

export default {
  name: 'MovieDetail',
  data: function() {
    return {
      starRating: 0,
      reviewComment: '',
    }
  },
  components: {
    KProgress,
    StarRating,
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
    setRating(rating) {
      this.starRating = rating;
    },
    updateMovieRating(movie) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_BASE_URL}${movie.id}/ratings/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
        data: {
          rate: this.starRating * 2,
          review: this.reviewComment
        }
      })
        .then((res) => {
          this.$store.dispatch('updateMovieRating', res.data) 
          this.reviewComment = ''
          console.log(this.$store.state.selectedMovie)
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
        this.starRating = 0;
        this.reviewComment = '';

        this.$store.dispatch('deleteMovieRating', rating.id)
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
          console.log('ㅁㅁㅁ', res)
          axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/api/v1/accounts/my_wishlist/',
            headers: {
              Authorization: `Bearer ${localStorage.getItem('jwt')}`
            }
          })
          .then((res) => {
            console.log('aaa')
            console.log(res)
            this.$store.dispatch('myWishList', res.data)
          })
          .then(res => {
            const likebtn = document.querySelector('#star')
            if (likebtn.classList.contains('far')) {
              likebtn.classList.remove('far')
              likebtn.classList.add('fas')
            } else {
              likebtn.classList.remove('fas')
              likebtn.classList.add('far')
            }
            console.log('bbb')
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
        })
          .then(res => {
            console.log(res)
          })  
    }
  },
  mounted() {
    const likebtn = document.querySelector('#changeLikeBtn')
    console.log(likebtn)
    console.log(this.$store.state.myWishList.includes(this.selectedMovie.id))
    if (this.$store.state.myWishList.includes(this.selectedMovie.id)) {
      console.log('aaa')
      likebtn.innerHTML = '<i class="fas fa-star" id="star"></i>'
      } else {
      console.log('bbb')
      likebtn.innerHTML = '<i class="far fa-star" id="star"></i>'
    }
  },
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);

.white {
  color: #EDEDED;
}

.vertical-line {
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

.actors {
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 10;        /* 최대 10줄까지만 보여주기 */
  -webkit-box-orient: vertical;
}

.overview {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 10;        /* 최대 10줄까지만 보여주기 */
  -webkit-box-orient: vertical;
}

.table {
  vertical-align: middle;
}

.fa-trash-alt:hover {
  transform: scale(1.3);  
}

#add-btn {
  background: none;
  border: none;
  padding: 0;
  font-size: 20px;
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


