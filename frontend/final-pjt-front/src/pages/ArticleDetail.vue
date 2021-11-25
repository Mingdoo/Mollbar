<template>
  <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black np">
    <div class="card border-0 bg-black">
      <div class="row justify-content-center">
        <div class="mt-5 col-6">
          <div class="card border-0 px-4 py-5">
            <h1 class="">💡 {{ selectedArticle.article_title }}</h1>
            <hr>
            <div class="container">
              <h6 style="height: 100%;" class="text-start">{{ selectedArticle.article_content }}</h6>
            </div>
            <hr>
            <p class="text-end mx-2">게시일 : {{ selectedArticle.created_at | moment('calendar') }}</p>
            <p class="text-end mx-2">수정일 : {{ selectedArticle.updated_at | moment('calendar') }}</p>
            <p class="mb-0 text-end mx-2">작성자 : {{ selectedArticle.username }}</p>
            <hr>
            <div class="">
              <button class="btn btn-danger mx-1 mb-0" @click="deleteArticle" v-if="isMyArticle">게시글 삭제</button>
              <button class="btn btn-success mx-1 mb-0" @click="updateArticle(selectedArticle)" v-if="isMyArticle">게시글 수정</button>
              <hr v-if="isMyArticle">
              <div class="row">
                <div class="col-10">
                  <input type="text" name="" id="" v-if="isLogin" v-model="userComment">
                </div>
                <div class="col-2">
                  <button class="btn btn-primary w-100 h-100" @click="commentSubmit" v-if="isLogin">댓글 생성</button>
                </div>
              </div> 
              <hr>
              
              <comment-list></comment-list>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/community/'

import axios from 'axios'
import Swal from 'sweetalert2'
import CommentList from '@/components/community/comments/commentList'

export default {
  name: "ArticleDetail",
  data() {
    return {
      userComment: null,
      // articleComments: null,
    }
  },
  components: {
    CommentList
  },
  computed: {
    selectedArticle() {
      return this.$store.state.selectedArticle
    },
    isMyArticle() {
      return this.selectedArticle.user === this.$store.state.userId
    },
    articleUrl() {
      return API_BASE_URL + `${this.selectedArticle.id}`
    },
    isLogin() {
      return this.$store.state.isLogin
    },
    
  },
  methods: {
    deleteArticle() {
      if (this.isMyArticle){
        const token = localStorage.getItem('jwt')
        axios({
          method: 'delete',
          url: this.articleUrl,
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
          .then(() => {
            this.$router.push({name: "CommunityHome"})
            Swal.fire({
              position: 'top',
              icon: 'success',
              title: '게시글이 삭제되었습니다.',
              showConfirmButton: false,
              timer: 1500
            })
          })
      }
    },
    commentSubmit() {
      console.log(this.articleUrl)
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: this.articleUrl + '/comments/',
        headers: {
          Authorization: `Bearer ${token}`,
        },
        data: {
          content: this.userComment
        }
      })
        .then((res) => {
          this.$store.dispatch('commentCreated', res.data)
          this.userComment = ''
          const Toast = Swal.mixin({
              toast: true,
              position: 'top-end',
              showConfirmButton: false,
              timer: 2000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
              })

            Toast.fire({
              icon: 'success',
              title: '댓글이 생성되었습니다.'
            })
        })
      },
    updateArticle(article) {
      if(this.isMyArticle){
        console.log(article)
        console.log(this.$store.state.selectedArticle)
        this.$router.push({name: "ArticleCreationForm", params: {article: this.$store.state.selectedArticle}})        
      }
    },
    },
  }

  
</script>

<style>

</style>