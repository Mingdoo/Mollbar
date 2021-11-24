<template>
  <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black np">
    <div class="card border-0 bg-black">
      <div class="row d-flex justify-content-center">
        <div class="mt-5 col-6">
          <div class="card border-0 px-4 py-5">
            <div v-if="!this.$route.params.article">
              <h1>✔ 게시글 생성</h1>
              <hr>
              <p><label for="title" class="h3">제목</label></p>
              <input type="text" name="" id="title" v-model="article_title" required class="w-100" placeholder="* 필수항목">
              
              <label for="content" class="h3">내용</label>
              <div class="form-floating">
                <textarea name="" id="content" class="form-control" v-model="article_content" required placeholder="* 필수항목" style="height: 200px"></textarea>
                <label for="content" class="">* 필수 항목</label>
              </div>
              <hr>
              <button class="btn btn-secondary w-100" @click="submitArticle(false)">게시글 생성</button>
            </div>
            <div v-else>
              <h1>🔍 게시글 수정</h1>
              <hr>
              <p><label for="title" class="h3">제목</label></p>
              <input type="text" name="" id="title" @input="article_title=$event.target.value" v-bind:value="this.$route.params.article.article_title" required class="w-100" placeholder="* 필수항목">
              
              <label for="content" class="h3">내용</label>
              <div class="form-floating">
                <textarea name="" id="content" class="form-control" @input="article_content=$event.target.value" required placeholder="* 필수항목" style="height: 200px" v-bind:value="this.$route.params.article.article_content"></textarea>
                <label for="content" class="">* 필수 항목</label>
              </div>
              <hr>
              <button class="btn btn-secondary w-100" @click="submitArticle(true)">게시글 수정</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'

const API_CREATION_URL = 'http://localhost:8000/api/v1/community/'
const token = localStorage.getItem('jwt')

export default {
  name: "ArticleCreate",
  data() {
    return {
      article_title: null,
      article_content: null,
    }
  },
  methods: {
    submitArticle(bool) {
      // console.log(this.article_content)
      // console.log(this.article_title)
      if (this.article_title && this.article_content){
        axios({
          method: 'post',
          url: API_CREATION_URL,
          headers: {
            Authorization: `Bearer ${token}`
          },
          data: {
            article_title: this.article_title,
            article_content: this.article_content
          }
        })
          .then(() => {
            // console.log(res)
            this.$router.push({ name: "CommunityHome"})
            if ( bool ) {
              Swal.fire({
                position: 'top',
                icon: 'success',
                title: '게시글 수정이 완료되었습니다!',
                showConfirmButton: false,
                timer: 1500
              })
            } else {
              Swal.fire({
                position: 'top',
                icon: 'success',
                title: '게시글 생성이 완료되었습니다!',
                showConfirmButton: false,
                timer: 1500
              })
            }
          })  
      } else {
        Swal.fire({
          position: 'top',
          icon: 'error',
          title: '필수 항목을 입력해주세요!',
          showConfirmButton: false,
          timer: 1500
        })
      }
    },
    updateArticle() {
      console.log(this.$route)
      // console.log(this.article_content)
      // console.log(this.article_title)
      if (this.article_title && this.article_content){
        axios({
          method: 'put',
          url: API_CREATION_URL + this.$route.params.article.id + '/',
          headers: {
            Authorization: `Bearer ${token}`
          },
          data: {
            article_title: this.article_title,
            article_content: this.article_content
          }
        })
          .then(() => {
            // console.log(res)
            this.$router.push({ name: "CommunityHome"})
          })  
      } else {
        alert('title과 content를 1자이상 입력하세요')
      }
  }},
  //mounted를 사용해서 update정보를 끌어옴
  mounted() {
    if (this.$route.params.article) {
      this.article_title = this.$route.params.article.article_title
      this.article_content = this.$route.params.article.article_content
    }
  }
}
</script>

<style>

</style>