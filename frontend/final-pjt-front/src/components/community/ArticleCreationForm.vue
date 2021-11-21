<template>
  <div>
    <div v-if="!this.$route.params.article">
      <h1>create</h1>
      <label for="title">title</label>
      <input type="text" name="" id="title" v-model="article_title" required>
      <label for="content">content</label>
      <input type="text" name="" id="content" v-model="article_content" required>
      <button @click="submitArticle">submit</button>
    </div>
    <div v-else>
      <h1>update</h1>
      <label for="title">title</label>
      <input type="text" name="" id="title" @input="article_title=$event.target.value" required v-bind:value="this.$route.params.article.article_title">
      <label for="content">content</label>
      <input type="text" name="" id="content" @input="article_content=$event.target.value" required :value="this.$route.params.article.article_content">
      <button @click="updateArticle">update</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
    submitArticle() {
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
          })  
      } else {
        alert('title과 content를 1자이상 입력하세요')
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
  }}
}
</script>

<style>

</style>