<template>
  <div class="">
    <div class="row">
      <h1>Profile page</h1>
      <div class="col-4">
        <img src="https://picsum.photos/200" alt="">
      </div>
      <div class="col-8">
        {{ userProfile.username }}님 환영합니다.
        <hr>
        <p>
          찜한 목록 : {{ userProfile.wishlist }}
        </p>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Profile",
  computed: {
    userProfile() {
      return this.$store.state.userProfile
    }
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/accounts/profile/${this.$store.state.userId}`,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('jwt')}`
      }
    })
      .then((res) => {
        this.$store.dispatch('userProfile', res.data)
      })
  }
}
</script>

<style>

</style>