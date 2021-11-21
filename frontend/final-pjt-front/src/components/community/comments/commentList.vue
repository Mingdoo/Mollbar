<template>
  <div>
    <h5 v-for="comment in comments" :key="comment.id">
      <div :id="`normalcomment${comment.id}`" class="commentformvisible">
        {{ comment.content }}
        <!-- {{ comment.comment_user }} -->
        <!-- {{ comment.created_at }} -->
        <button class="btn btn-primary" v-if="comment.comment_user === $store.state.userId" @click="updateComment(comment)">Edit</button>
        <button class="btn btn-warning" v-if="comment.comment_user === $store.state.userId" @click="deleteComment(comment)">Delete</button>
      </div>
      <div :id="`editcomment${comment.id}`" class="commentformhidden">
        <input type="text" name="" :value="comment.content" @input="userEditInput = $event.target.value">
        <button class="btn btn-warning" @click="editComment(comment)">확인</button>
        <button class="btn btn-primary" @click="cancelEditComment(comment)">취소</button>
      </div>
    </h5>
  </div>
</template>

<script>
const API_BASE_URL = 'http://127.0.0.1:8000/api/v1/community/'


import axios from 'axios'
export default {
  name: "CommentList",
  data() {
    return {
      userEditInput: '',
    }
  },
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
      const token = localStorage.getItem('jwt')
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
    },
    updateComment(comment) {
      const normalcomment = document.querySelector(`#normalcomment${comment.id}`)
      normalcomment.classList.remove('commentformvisible')
      normalcomment.classList.add('commentformhidden')

      const editcomment = document.querySelector(`#editcomment${comment.id}`)
      editcomment.classList.remove('commentformhidden')
      editcomment.classList.add('commentformvisible')

      // console.log(normalcomment)
    },
    editComment(comment) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'put',
        url: `${API_BASE_URL}${this.selectedArticle.id}/comments/${comment.id}/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
        data: {
          content: this.userEditInput
        }
      })
        .then((res) => {
          console.log(res)
        })
      const normalcomment = document.querySelector(`#normalcomment${comment.id}`)
      normalcomment.classList.add('commentformvisible')
      normalcomment.classList.remove('commentformhidden')

      const editcomment = document.querySelector(`#editcomment${comment.id}`)
      editcomment.classList.add('commentformhidden')
      editcomment.classList.remove('commentformvisible')
    }
  }
}
</script>

<style>
.commentformvisible {
  visibility: visible;
}

.commentformhidden {
  display: none;
}
</style>