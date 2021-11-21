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
// import axios from 'axios'
export default {
  name: "CommentList",
  computed: {
    comments() {
      return this.$store.state.selectedArticleComments
    },
  },
  methods: {
    deleteComment(comment) {
      // axios({
        
      //   })
      console.log(comment.id)
    }
  }
}
</script>

<style>

</style>