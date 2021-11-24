<template>
  <div class="container mt-5 mb-3 d-flex">
    <div class="row container-fluid mt-5">
      <div class="row">
      </div>
      <div class="row input-group">
        <h1 class="np mb-3 text-white">같이 영화를 찾아봐요</h1>
        <div class="col-4">
          <h2 class="text-white np">제목</h2>
        </div>
        <div class="col-4">
          <h2 class="text-white np">장르</h2>
        </div>
        <div class="col-4">
          <h2 class="text-white np">최소 평점</h2>
        </div>
        <div class="col-md-4">
          <input type="text" name="" id="" placeholder="영화 제목을 입력해주세요" v-model="searchName" @keyup.enter="searchMovie">
        </div>
        <div class="col-md-4">
          <select name="" id="" class="form-select form-select-lg np" v-model="genre" style="line-height: inherit; font-size: 22px">
            <option value="" selected>전체 장르</option>
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
        <div class="col-md-4">
          <input type="number" name="" id="" min=0 max=10 placeholder="최소 평점" v-model="min_rate">
        </div>
        <div>
          <button class="btn btn-outline-secondary my-3 w-100 np" @click="searchMovie">검색</button>
        </div>
        <hr>
      </div>
        <search-list v-for="searchResult in searchResults" :key="searchResult.id" :search-result="searchResult"></search-list>
      <div v-if="!searchResults">
        <p class="np font-white" style="font-size: 500px">..텅..</p>
      </div>
    </div>
  </div>
</template>

<script>
import SearchList from '@/components/movies/SearchList'
import axios from 'axios'
const API_SEARCH_URL = 'http://127.0.0.1:8000/api/v1/movies/search/'

export default {
  name: "Search",
  components: {
    SearchList
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
    isSearched(e) {
      console.log(e)
      return ''
    }
  },
  methods: {
    searchMovie() {
      axios({
        method: 'get',
        url: API_SEARCH_URL,
        params: {
          query: this.searchName,
          genre: this.genre,
          min_rate: this.min_rate,
        }
      })
        .then((res) => {
          this.$store.dispatch('searchMovie', res.data)
        })
        .then(() => {
          this.$router.push({name: "Search"})
        })
        .catch((err) => {
          alert(err)
        })
    }
  }
}
</script>

<style>

</style>