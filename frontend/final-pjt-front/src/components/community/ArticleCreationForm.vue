<template>
  <div>
    <h1>create</h1>
    <label for="title">title</label>
    <input type="text" name="" id="title" v-model="article_title" required>
    <label for="content">content</label>
    <input type="text" name="" id="content" v-model="article_content" required>
    <button @click="submitArticle">submit</button>
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
    }
  }
}
</script>

<style>

</style>