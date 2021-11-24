<template>
  <tr @click="selectArticle(article)" style="cursor: pointer;" class="text-white np">
    <th scope="row">{{ article.id }}</th>
    <td>{{ article.article_title }}</td>
    <td>{{ article.username }}</td>
    <td>{{ article.created_at | moment('calendar') }}</td>
    <td>{{ article.updated_at | moment('calendar') }}</td>
  </tr>
  
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
    selectArticle(article) {
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
          this.$router.push({path: `community/${article.id}`})
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