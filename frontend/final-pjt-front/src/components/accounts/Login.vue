<template>
  <div class="row">
    <form action="" class="my-2">
        <label for="usrname">아이디</label>
        <input 
          type="text" id="usrname" name="usrname" 
          required v-model="credentials.id"
          class="mb-3"
        >

        <label for="psw">비밀번호</label>
        <input 
          type="password" id="psw" name="psw"
          required
          v-model="credentials.password"
          @keyup.enter="loginEvent" class="mb-5"
        >
        <input type="submit" value="Submit" @click="loginEvent">
      </form>
  </div>
</template>

<script>
import axios from 'axios';
const BASE_URL = 'http://127.0.0.1:8000/'

export default {
  name: "Login",
  data() {
    return {
      credentials: {},
      loginUrl: BASE_URL + '/accounts/login/'
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
          console.log(res)
        })
        .catch((err)=> {
          console.log(err)
        })
    }
  },
}
</script>

<style>

</style>