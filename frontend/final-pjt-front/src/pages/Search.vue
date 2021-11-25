<template>
  <div class="container mt-5 mb-3 d-flex">
    <div class="row container-fluid mt-5">
      <div class="row">
      </div>
      <div class="row input-group">
        <h1 class="np mb-5 text-white">같이 영화를 찾아봐요</h1>
        <hr>
        <div class="col-lg-4">
          <h2 class="text-white np">제목</h2>
          <input type="text" name="" id="" placeholder="영화 제목을 입력해주세요" v-model="searchName" @keyup.enter="searchMovie">
        </div>
        <div class="col-lg-4">
          <h2 class="text-white np">장르</h2>
          <select name="" id="" class="form-select form-select-lg np" v-model="genre" style="line-height: inherit; font-size: 22px">
            <option value="" selected>최신 영화</option>
            <option value="12" >어드벤쳐</option>
            <option value="14" >판타지</option>
            <option value="16" >애니메이션</option>
            <option value="18" >드라마</option>
            <option value="27" >호러</option>
            <option value="28" >액션</option>
            <option value="35" >코미디</option>
            <option value="36" >역사</option>
            <option value="37" >서부</option>
            <option value="53" >스릴러</option>
            <option value="80" >범죄</option>
            <option value="99" >다큐멘터리</option>
            <option value="878" >SF</option>
            <option value="9648" >미스터리</option>
            <option value="10402" >음악</option>
            <option value="10749" >로맨스</option>
            <option value="10751" >가족</option>
            <option value="10752" >전쟁</option>
            <option value="10770" >TV 영화</option>
          </select>
        </div>
        <div class="col-lg-4">
          <h2 class="text-white np">최소 평점</h2>
          <star-rating
          :increment="0.1"
          :glow="3"
          :clearable=true
          :show-rating="false"
          v-model="min_rate"
          class="justify-content-center" 
          >
          </star-rating>
        </div>
        <div>
          <button class="btn btn-outline-secondary my-3 w-100 np" @click="searchMovie">검색</button>
        </div>
        <hr>
      </div>
      <transition-group
      name="fade"
      mode="out-in"
      class="row"
      :key="1"
      v-if="searchResults"
      >
      <search-list v-for="searchResult in searchResults" :key="searchResult.id" :search-result="searchResult"></search-list>
      <div v-if="!searchResults">
        <p class="np font-white" style="font-size: 500px">..텅..</p>
      </div>
      </transition-group>
      <div v-else>
        <p style="font-size: 500px" class="np">..텅..</p>
      </div>
    </div>
  </div>
</template>

<script>
import SearchList from '@/components/movies/SearchList'
import StarRating from 'vue-star-rating';
import axios from 'axios'
const API_SEARCH_URL = 'http://127.0.0.1:8000/api/v1/movies/search/'

export default {
  name: "Search",
  components: {
    SearchList,
    StarRating,
  },
  data() {
    return {
      searchName: '',
      genre: '',
      min_rate: 0,
    }
  },
  computed: {
    searchResults() {
      return this.$store.state.searchResults
    },
  },
  methods: {
    searchMovie() {
      console.log(this.min_rate * 2)
      axios({
        method: 'get',
        url: API_SEARCH_URL,
        params: {
          query: this.searchName,
          genre: this.genre,
          min_rate: this.min_rate * 2,
        }
      })
        .then((res) => {
          this.$store.dispatch('searchMovie', res.data)
        })
        .then(() => {
          this.$router.push({name: "Search", params: {query: this.searchName}}).catch(() => {})
        })
        .catch((err) => {
          alert(err)
        })
    }
  },
  created() {
    console.log(this.$route.params.query)
  }
}
</script>

<style>
search-list {
  transition: visibility 0s linear 0.5s, opacity 0.5s linear, font 0.05s linear;
}
</style>