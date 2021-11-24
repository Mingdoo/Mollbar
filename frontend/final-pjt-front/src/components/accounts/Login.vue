<template>
  <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black">
    <div class="card card0 border-0 bg-black">
        <div class="row d-flex">
            <div class="col-lg-6">
                <div class="card1 pb-5">
                    <div class="row px-3 justify-content-center mt-4 mb-5 border-line"> <img src="../../assets/instagram_profile_image.png" class="image"> </div>
                </div>
            </div>
            <div class="col-lg-6 mt-5">
                <div class="card2 card border-0 px-4 py-5">
                    <div class="row px-3"> <label class="mb-1">
                            <h6 class="mb-0 text-sm">아이디</h6>
                        </label> <input class="mb-4" type="text" name="email" placeholder="아이디를 입력하세요" required v-model="credentials.username"> </div>
                    <div class="row px-3"> <label class="mb-1">
                            <h6 class="mb-0 text-sm">비밀번호</h6>
                        </label> <input type="password" name="password" placeholder="비밀번호를 입력하세요" v-model="credentials.password" @keyup.enter="loginEvent"> </div>
                    <div class="row mb-3 px-3"> <button type="submit" class="btn btn-secondary text-center mt-4" @click="loginEvent">Login</button> </div>
                    <div class="row mb-4 px-3"> <small class="font-weight-bold">Don't have an account? <router-link class="text-danger text-decoration-none" to="/signup">Register</router-link></small> </div>
                </div>
            </div>
        </div>
        <div class="bg-blue py-4">
            <div class="row px-3"> <small class="ml-4 ml-sm-5 mb-2">Copyright &copy; 2019. All rights reserved.</small>
            </div>
        </div>
    </div>
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
        .then(() => {
          axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/api/v1/accounts/my_wishlist/',
            headers: {
              Authorization: `Bearer ${localStorage.getItem('jwt')}`
            }
          })
          .then((res) => {
            this.$store.dispatch('myWishList', res.data)
          })
          .catch((err) => {
            console.log(err)
          })
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