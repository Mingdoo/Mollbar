<template>
  <div class="row">
    <h1>Signup Page</h1>
    <div class="col-6">

      <label for="usrname">아이디</label>
      <input 
        type="text" id="usrname" name="usrname" 
        required v-model="credentials.username"
        pattern="^([a-z0-9_]){6,50}$"
        title="warning"
        class="mb-3"
      >

      <label for="psw">비밀번호</label>
      <input 
        type="password" id="psw" name="psw"
        pattern="(?=.[a-z])(?=.*\d)(?=.*[A-Z]).{8,50}"
        title="영문 대소문자, 숫자를 꼭 포함하여 8자 이상 50자 미만으로 작성해주세요."
        required
        v-model="credentials.password"
        class="mb-3"
      >
      <label for="pswconf">비밀번호 확인</label>
      <input type="password" name="pswconf" id="pswconf" v-model="credentials.passwordConfirmation" @keyup.enter="signUp" class="mb-3">
      
      <label for="eml">이메일</label>
      <input type="email" name="" id="eml" v-model="credentials.email" class="mb-3">
      <input type="submit" value="Submit" class="accountsubmit" @click="signUp" :class="{'visible': isPasswordConfirmationValid && isPasswordContainsCapital && isPasswordContainsLower && isPasswordContainsNumber && isPasswordLengthValid }">


    </div>
    <div class="col-6 message">
      <h4>아이디 규칙</h4>
      <p id="idconfirmation" class="invalid mt-3"><b>숫자 또는 소문자</b>로만 6자 이상 포함해주세요</p>
      <h4>패스워드 규칙</h4>
      <p id="capital" class="invalid mt-3"><b>대문자</b>를 포함해주세요</p>
      <p id="lowercase" class="invalid"><b>소문자</b>를 포함해주세요</p>
      <p id="number" class="invalid"><b>숫자</b>를 포함해주세요</p>
      <p id="length" class="invalid mb-4"><b>8자</b> 이상을 포함해주세요</p>
      <p id="passwordconfirmation" class="invalid mb-4"><b>동일한</b> 비밀번호를 입력해주세요</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
            alert("가입되었습니다.")
            this.$router.push({name: 'Login'})
          })
          .catch(() => {
            // console.log(err)
            alert("중복된 이름이 있습니다")
            // this.$router.push({name: 'Login'})
          })
      }
    },

  },
  updated() {
    // console.log(
    //   this.isUsernameLengthValid,
    //   this.isPasswordContainsNumber,
    //   this.isPasswordContainsCapital,
    //   this.isPasswordLengthValid,
    //   this.isPasswordContainsLower,
    //   this.isPasswordConfirmationValid
    // )
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

.visible {
  background-color: lawngreen !important;
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
</style>