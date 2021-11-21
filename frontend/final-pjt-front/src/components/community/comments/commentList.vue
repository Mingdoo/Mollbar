<template>
  <div>
    <h5 v-for="comment in comments" :key="comment.id">
      {{ comment.content }}
      {{ comment.comment_user }}
      {{ comment.created_at }}
      <button class="btn btn-warning" v-if="comment.comment_user === $store.state.userId" @click="deleteComment(comment)">Delete</button>
    </h5>
  </div>
</template>

<script>
const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/community/'
const token = localStorage.getItem('jwt')

import axios from 'axios'
export default {
  name: "CommentList",
  computed: {
    comments() {
      return this.$store.state.selectedArticleComments
    },
    selectedArticle() {
      return this.$store.state.selectedArticle
    }
  },
  methods: {
    deleteComment(comment) {
      axios({
        method: 'delete',
        url: `${API_BASE_URL}${this.selectedArticle.id}/comments/${comment.id}/`,
        headers: {
          Authorizaion: `Bearer ${token}`
        }
        })
          .then((res) => {
            console.log(res)
          })
      // console.log(`${API_BASE_URL}${this.selectedArticle.id}/comments/${comment.id}/`)
    }
  }
}
</script>

<style>

</style>