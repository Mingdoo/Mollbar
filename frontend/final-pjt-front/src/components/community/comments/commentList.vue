<template>
  <div class="np">
    <h1>댓글 목록</h1>
    <hr>
    <div v-if="comments.length">
      <h5 v-for="comment in comments" :key="comment.id">
        <div :id="`normalcomment${comment.id}`" class="commentformvisible row align-items-center">
          <div class="col-2 text-success fs-6">
            {{comment.username}}
          </div>
          <div class="col-5 text-start fs-6">
            {{ comment.content }}
          </div>
          <div class="col-2 fs-6">
            {{ comment.created_at | moment('calendar') }}
          </div>
          <div class="col-3">
            <button class="btn btn-danger mx-1" v-if="comment.comment_user === $store.state.userId" @click="deleteComment(comment)">삭제</button>
            <button class="btn btn-success mx-1" v-if="comment.comment_user === $store.state.userId" @click="updateComment(comment)">수정</button>
          </div>
        </div>
        <div :id="`editcomment${comment.id}`" class="commentformhidden">
          <input type="text" name="" :value="comment.content" @input="userEditInput = $event.target.value">
          <button class="btn btn-primary mx-1 my-1" @click="editComment(comment)">확인</button>
          <button class="btn btn-danger mx-1 my-1" @click="cancelEditComment(comment)">취소</button>
        </div>
      </h5>
    </div>
    <div v-else>
      <p style="font-size: 15px">첫 댓글을 달아보세요!</p>
    </div>
    <hr v-if="comments">
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
          Authorization: `Bearer ${token}`
        }
        })
          .then(() => {
            this.$store.dispatch('deleteComment', comment.id)
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
          this.$store.dispatch('editComment', res.data)
        })
      const normalcomment = document.querySelector(`#normalcomment${comment.id}`)
      normalcomment.classList.add('commentformvisible')
      normalcomment.classList.remove('commentformhidden')

      const editcomment = document.querySelector(`#editcomment${comment.id}`)
      editcomment.classList.add('commentformhidden')
      editcomment.classList.remove('commentformvisible')
    },
    cancelEditComment(comment) {
      const normalcomment = document.querySelector(`#normalcomment${comment.id}`)
      normalcomment.classList.add('commentformvisible')
      normalcomment.classList.remove('commentformhidden')

      const editcomment = document.querySelector(`#editcomment${comment.id}`)
      editcomment.classList.add('commentformhidden')
      editcomment.classList.remove('commentformvisible')
    }
  },
  created() {
    
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