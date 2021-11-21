<template>
  <div>
    <h1>{{ selectedArticle.article_title }}</h1>
    <h4>{{ selectedArticle.article_content }}</h4>
    <button class="btn btn-warning" @click="deleteArticle" v-if="isMyArticle">Delete</button>
    <input type="text" name="" id="" v-if="isLogin" v-model="userComment">
    <button class="btn btn-primary mt-3" @click="commentSubmit">Submit</button>
    <comment-list></comment-list>
  </div>
</template>

<script>
const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/community/'

import axios from 'axios'
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
        })
    }
  },
  // beforeUpdate() {
  //   const token = localStorage.getItem('jwt')
  //   axios({
  //     method: 'get',
  //     url: this.articleUrl + '/comments/',
  //     headers: {
  //       Authorization: `Bearer ${token}`,
  //     },
  //   })
  //     .then((res) => {
  //       console.log(res)
  //       this.articleComments = res.data
  //     }) 
  //     .catch(() => {
  //       this.articleComments = ''
  //     })
  //   }
  }

  
</script>

<style>

</style>