<template>
  <div class="row">
    <h1>Login Page</h1>
    <div class="col-6">
      <form action="" class="my-2">
        <label for="usrname">아이디</label>
        <input 
          type="text" id="usrname" name="usrname" 
          required v-model="credentials.id"
          pattern="^([a-z0-9_]){6,50}$"
          title="warning"
          class="mb-3"
        >

        <label for="psw">비밀번호</label>
        <input 
          type="password" id="psw" name="psw"
          pattern="(?=.*\d)(?=.*[A-Z]).{8,}"
          title="영문 대소문자, 숫자를 꼭 포함하여 8자 이상 50자 미만으로 작성해주세요."
          required
          v-model="credentials.password"
          class="mb-3"
        >
        <label for="pswconf">비밀번호 확인</label>
        <input type="password" name="pswconf" id="pswconf" v-model="credentials.passwordConfirmation" @keyup.enter="signUp" class="mb-5">
        <input type="submit" value="Submit" @click="signUp">
      </form>

    </div>
    <div class="col-6 message">
      <h4>패스워드 규칙</h4>
      <p id="capital" class="invalid mt-5"><b>대문자</b>를 포함해주세요</p>
      <p id="number" class="invalid"><b>숫자</b>를 포함해주세요</p>
      <p id="length" class="invalid mb-4"><b>8자</b> 이상을 포함해주세요</p>
      <p id="passwordconfirmation" class="invalid mb-4"><b>동일한</b> 비밀번호를 입력해주세요</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/accounts/signup/'
var numbers = /[0-9]/g;
var upperCaseLetters = /[A-Z]/g;

export default {
  name: "SignUp",
  data() {
    return {
      credentials: {
      },
      isValid: false
    }
  },
  methods: {
    signUp: function() {
      axios({
        method: 'post',
        url: SERVER_URL,
        data: this.credentials
      })
        .then(() => {
          this.$router.push({name: 'Login'})
        })
        .catch((err) => {
          console.log(err)
          this.$router.push({name: 'Login'})
        })
    },

  },
  updated() {
    var myInput = document.getElementById("psw");
    var myInputConfirmation = document.getElementById("pswconf");
    var capital = document.getElementById("capital");
    var number = document.getElementById("number");
    var length = document.getElementById("length");
    var confirmation = document.getElementById("passwordconfirmation");
    
    if(myInput.value.match(numbers)) {
      number.classList.remove("invalid");
        number.classList.add("valid");
      } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
      }
      if(myInput.value.match(upperCaseLetters)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
      } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
      }
      if(myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
      } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
      }
      if(myInput.value !== myInputConfirmation.value){
        confirmation.classList.remove("valid");
        confirmation.classList.add("invalid")
      } else {
        confirmation.classList.remove("invalid");
        confirmation.classList.add("valid")
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
input[type=submit] {
  background-color: #04AA6D;
  color: white;
}

/* Style the container for inputs */
.container {
  background-color: #f1f1f1;
  padding: 20px;
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
  left: -35px;
  content: "✔";
}

/* Add a red text color and an "x" icon when the requirements are wrong */
.invalid {
  color: red;
}

.invalid:before {
  position: relative;
  left: -35px;
  content: "❌";
}
</style>