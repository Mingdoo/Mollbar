<template>
  <div>
    <router-link :to="`/community/${article.id}`" @click.native="selectArticle">{{ article.article_title }}</router-link> |
    <h5 class="d-inline">작성자 : {{ article.username }}</h5>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "ArticleCard",
  props: {
    article: Object
  },
  data() {
    return {
      comments: null,
    }
  },
  methods: {
    selectArticle() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/community/${this.article.id}/comments/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          this.$store.dispatch('setComments', res.data)
        }) 
        .catch(() => {
          this.$store.dispatch('setComments', [])
        })
      this.$store.dispatch('selectArticle', this.article)
    }
  }
}
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
</script>

<style>

</style>