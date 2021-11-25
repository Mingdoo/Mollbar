<template>
  <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black">
    <div class="card card0 border-0 bg-black">
        <div class="row d-flex justify-content-center">
            <div class="mt-4 col-xl-4">
                <div class="card1 card border-0 px-4 py-5">
                <h1 class="np">회원가입</h1>
                    <div class="row px-3"> <label class="mb-1">
                      <h6 class="mb-0 text-sm np">아이디</h6></label>
                      <input class="mb-4" type="text" name="username" id="usrname" placeholder="아이디를 입력하세요" required v-model="credentials.username" pattern="^([a-z0-9_]){6,50}$" title="아이디를 6자 이상 입력해주세요.">
                    </div>
                    <div class="row px-3"> <label class="mb-1">
                      <h6 class="mb-0 text-sm np">비밀번호</h6></label>
                      <input class="mb-4" type="password" name="password" id="psw" placeholder="비밀번호를 입력하세요" v-model="credentials.password" pattern="(?=.[a-z])(?=.*\d)(?=.*[A-Z]).{8,50}" title="영문 대소문자, 숫자를 꼭 포함하여 8자 이상 50자 미만으로 작성해주세요.">
                    </div>
                    <div class="row px-3"> <label class="mb-1">
                      <h6 class="mb-0 text-sm np">비밀번호 확인</h6></label>
                      <input class="mb-4" type="password" name="passwordconfirmation" id="pswconf" placeholder="비밀번호를 입력하세요" v-model="credentials.passwordConfirmation" @keyup.enter="signUp">
                    </div>
                    <div class="row px-3"> <label class="mb-1">
                      <h6 class="mb-0 text-sm np">이메일</h6></label>
                      <input class="mb-4" type="email" name="" placeholder="* 선택사항 (ex. mollbar@ssafy.com)" v-model="credentials.email">
                    </div>
                    <div class="row px-3">
                      <div class="card card2 px-4 py-5 border-0">
                        <h4 class="np">아이디 규칙</h4>
                        <p id="idconfirmation" class="invalid mt-3 np"><b>숫자 또는 소문자</b>로만 6자 이상 포함해주세요</p>
                        <h4 class="np mt-3">패스워드 규칙</h4>
                        <p id="capital" class="invalid mt-3 np"><b>대문자</b>를 포함해주세요</p>
                        <p id="lowercase" class="invalid np"><b>소문자</b>를 포함해주세요</p>
                        <p id="number" class="invalid np"><b>숫자</b>를 포함해주세요</p>
                        <p id="length" class="invalid np"><b>8자</b> 이상을 포함해주세요</p>
                        <p id="passwordconfirmation" class="invalid mb-4 np"><b>동일한</b> 비밀번호를 입력해주세요</p>
                      </div>
                    </div>
                    <div class="row mb-3 px-3"> <button type="submit" class="btn btn-secondary text-center mt-4" :class="{'is-valid': isPasswordConfirmationValid && isPasswordContainsCapital && isPasswordContainsLower && isPasswordContainsNumber && isPasswordLengthValid }" @click="signUp">회원가입</button> </div>
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
import axios from 'axios'
import Swal from 'sweetalert2';
const SERVER_URL = 'http://127.0.0.1:8000/api/v1/accounts/signup/'
var numbers = /[0-9]/g;
var upperCaseLetters = /[A-Z]/g;
var lowerCaseLetters = /[a-z]/g;

export default {
  name: "SignUp",
  data() {
    return {
      credentials: {
      },
      isUsernameLengthValid: false,
      isPasswordContainsNumber: false,
      isPasswordContainsCapital: false,
      isPasswordLengthValid: false,
      isPasswordContainsLower: false,
      isPasswordConfirmationValid: false
    }
  },
  methods: {
    signUp: function() {
      //모든 조건을 만족했을 때
      if (
        this.credentials.password === this.credentials.passwordConfirmation &&
        this.isPasswordContainsNumber && this.isPasswordContainsCapital &&
        this.isPasswordLengthValid && this.isPasswordContainsLower &&
        this.isPasswordConfirmationValid && this.isUsernameLengthValid
        ){
        axios({
          method: 'post',
          url: SERVER_URL,
          data: this.credentials
        })
          .then(() => {
            // alert("가입되었습니다.")
            this.$router.push({name: 'Login'})
            Swal.fire({
              position: 'top',
              icon: 'success',
              title: '회원가입이 완료되었습니다.',
              showConfirmButton: false,
              timer: 1500
            })
          })
          .catch(() => {
            const Toast = Swal.mixin({
              toast: true,
              position: 'top',
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
              })

            Toast.fire({
              icon: 'error',
              title: '중복된 아이디가 있습니다.'
            })
          })
      }
    },

  },
  updated() {
    //input
    var userName = document.getElementById("usrname");
    var myInput = document.getElementById("psw");
    var myInputConfirmation = document.getElementById("pswconf");

    //alert
    var idConfirmation = document.getElementById("idconfirmation");
    var capital = document.getElementById("capital");
    var lowercase = document.getElementById("lowercase");
    var number = document.getElementById("number");
    var length = document.getElementById("length");
    var confirmation = document.getElementById("passwordconfirmation");

    if ((userName.value.match(numbers) || userName.value.match(lowerCaseLetters) && userName.value.length >= 6 && userName.value.length <= 50)){
      idConfirmation.classList.remove("invalid");
      idConfirmation.classList.add("valid");
      this.isUsernameLengthValid = true
    } else {
      idConfirmation.classList.remove("valid");
      idConfirmation.classList.add("invalid");
      this.isUsernameLengthValid = false
    }
    if(myInput.value.match(numbers)) {
      number.classList.remove("invalid");
      number.classList.add("valid");
      this.isPasswordContainsNumber = true
    } else {
      number.classList.remove("valid");
      number.classList.add("invalid");
      this.isPasswordContainsNumber = false
    }
    if(myInput.value.match(upperCaseLetters)) {
      capital.classList.remove("invalid");
      capital.classList.add("valid");
      this.isPasswordContainsCapital = true
    } else {
      capital.classList.remove("valid");
      capital.classList.add("invalid");
      this.isPasswordContainsCapital = false
    }
    if(myInput.value.length >= 8) {
      length.classList.remove("invalid");
      length.classList.add("valid");
      this.isPasswordLengthValid = true
    } else {
      length.classList.remove("valid");
      length.classList.add("invalid");
      this.isPasswordLengthValid = false
    }
    if(myInput.value !== myInputConfirmation.value){
      confirmation.classList.remove("valid");
      confirmation.classList.add("invalid");
      this.isPasswordConfirmationValid = false
    } else {
      confirmation.classList.remove("invalid");
      confirmation.classList.add("valid")
      this.isPasswordConfirmationValid = true
    }
    if(myInput.value.match(lowerCaseLetters)) {
      lowercase.classList.remove("invalid")
      lowercase.classList.add("valid")
      this.isPasswordContainsLower = true
    } else {
      lowercase.classList.remove("valid")
      lowercase.classList.add("invalid")
      this.isPasswordContainsLower = false
    }
  }
}
</script>

<style>
input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
}

/* Style the submit button */
.accountsubmit {
  background-color: red;
  /* color: white; */
}

.is-valid {
  background-color: #0F52BA !important;
  border: none !important;
}

/* The message box is shown when the user clicks on the password field */
#message {
  display:none;
  background: #f1f1f1;
  color: #000;
  position: relative;
  padding: 20px;
  margin-top: 10px;
}

#message p {
  padding: 10px 35px;
  font-size: 18px;
}

/* Add a green text color and a checkmark when the requirements are right */
.valid {
  color: green;
}

.valid:before {
  position: relative;
  left: -5px;
  content: "✔";
}

/* Add a red text color and an "x" icon when the requirements are wrong */
.invalid {
  color: red;
}

.invalid:before {
  position: relative;
  left: -5px;
  content: "❌";
}

.image {
  width: 600px;
}
</style>