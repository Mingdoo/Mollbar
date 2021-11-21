<template>
  <div class="row">
    <label for="usrname">아이디</label>
    <input 
      type="text" id="usrname" name="usrname" 
      required v-model="credentials.username"
      class="mb-3"
    >

    <label for="psw">비밀번호</label>
    <input 
      type="password" id="psw" name="psw"
      required
      v-model="credentials.password"
      @keyup.enter="loginEvent" class="mb-5"
    >
    <input type="submit" value="Submit" id="loginButton" @click="loginEvent">
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = 'http://127.0.0.1:8000/'

export default {
  name: "Login",
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loginUrl: BASE_URL + 'api/v1/accounts/token/'
    }
  },
  methods: {
    loginEvent(){
      axios({
        method: 'post',
        url: this.loginUrl,
        data: this.credentials,
      })
        .then((res) => {
          localStorage.setItem('jwt', res.data.access)
          this.$store.dispatch('changeLogged')
          this.$store.dispatch('setJwtToken', res.data.access)
          this.$router.push({name: "Home"})
        })
        .catch(()=> {
          alert('로그인에 실패하였습니다. 아이디와 비밀번호를 다시 입력해주세요.')
        })
    },
  },
  updated() {
    const btn = document.querySelector('#loginButton')
    if (this.credentials.username && this.credentials.password) {
      btn.classList.add('blueButton')
    } else {
      btn.classList.remove('blueButton')
    }
  }
}
</script>

<style>
.blueButton {
  background-color: chartreuse;
}
</style>