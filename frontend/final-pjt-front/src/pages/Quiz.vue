<template>
  <div class="d-flex justify-content-center">
      
    <div v-if="showScore">
        <b-card
        title="Results"
        style="max-width: 20rem;"
        >
        You Scored {{score}} of {{questions.length}}
        </b-card>
    </div>
    <div class="card-q" v-else>
    <span v-if="!startQuiz">
      <b-card
        img-src="https://imgtoolkit.culturebase.org/?color=FFFFFF&quality=8&ar_ratio=1.3&format=jpg&file=http%3A%2F%2Fdata.heimat.de%2Fpics%2F5%2Fe%2F0%2Fa%2Fd%2Fpic_1387803322_5e0ad29c4026d5f9a038cfc4c13840dc.jpeg&do=cropOut&width=1200&height=450"
        img-alt="Image"
        img-top
        title="영잘알 테스트 - 한국영화 편"
        style="max-width: 20rem;"
        class="mb-2 overflow-hidden"
      >
      <b-card-text>
        <p>2000년 이후 개봉한 한국영화 포스터의 일부분과 4개의 보기가 주어집니다.</p>
        <p>포스터에 맞는 영화 제목을 골라주세요.</p>
        <p>총 10개의 문제가 주어지며, 각 문제당 10초의 제한 시간이 있습니다.</p>
      </b-card-text>
      <b-button @click="startQuizFunc()">Start Quiz</b-button>
    </b-card>
    </span>

    <span v-else>
    <b-card 
        title="영잘알 테스트 - 한국영화 편"
        style="max-width: 20rem; position: relative;"
        class="mb-2 overflow-hidden"
        :questions="questions"
    >
    <!-- <b-card-img
      id="poster-image"
      v-model="questions"
      :src="'https://image.tmdb.org/t/p/w500' + questions[currentQuestion].poster_path"
      bottom
    >
    </b-card-img> -->
    <div 
      id="poster-image"
      :style="{backgroundImage: `url(https://image.tmdb.org/t/p/w500${questions[currentQuestion].poster_path})`}"
    >
    </div>
    <b-card-text id="question">
      Question No.{{currentQuestion + 1}} of {{questions.length}}
    </b-card-text>
    <br>
    <b-progress
        variant="warning"
        :max="10"
        :value="countDown"
        height="4px"
      ></b-progress>
  
    <b-card-text>
      <span style="font-size: 40px;"><strong>{{countDown}} </strong></span>
    </b-card-text>

    <!-- <b-card-image>
      {{questions[currentQuestion].poster_path}}
    </b-card-image> -->
    <!-- <b-card-text>
      {{questions[currentQuestion].questionText}}
    </b-card-text> -->
    <div class="answer-section">
      <b-button :key="index" v-for="(option, index) in questions[currentQuestion].options" @click="handleAnswerClick(option.isCorrect)" class="ans-option-btn" variant="primary">{{option.title}}</b-button>
    </div>
  </b-card>
    </span>
  </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            currentQuestion: 0,
            showScore: false,
            score:0,
            countDown : 10,
            timer:null,
            startQuiz: false,

            questions : 
              [
                  {
                      "poster_path": "/5j2YVF7VouLG0Ze96SEsj4DnVQM.jpg",
                      "options": [
                          {
                              "title": "신과함께-죄와 벌",
                              "isCorrect": true
                          },
                          {
                              "title": "범죄와의 전쟁: 나쁜놈들 전성시대",
                              "isCorrect": false
                          },
                          {
                              "title": "폰",
                              "isCorrect": false
                          },
                          {
                              "title": "어린 신부",
                              "isCorrect": false
                          }
                      ]
                  },
                  {
                      "poster_path": "/ucRS5itC1Ea4kgg8h8QBlCo3qnG.jpg",
                      "options": [
                          {
                              "title": "김복남 살인 사건의 전말",
                              "isCorrect": true
                          },
                          {
                              "title": "하울링",
                              "isCorrect": false
                          },
                          {
                              "title": "박쥐",
                              "isCorrect": false
                          },
                          {
                              "title": "사자",
                              "isCorrect": false
                          }
                      ]
                  },
                  {
                      "poster_path": "/2MCy07o0FHQYjigKim5bHF78267.jpg",
                      "options": [
                          {
                              "title": "악인전",
                              "isCorrect": false
                          },
                          {
                              "title": "미녀는 괴로워",
                              "isCorrect": false
                          },
                          {
                              "title": "끝까지 간다",
                              "isCorrect": true
                          },
                          {
                              "title": "북촌방향",
                              "isCorrect": false
                          }
                      ]
                  },
                  {
                      "poster_path": "/pUwY1vftUyxJvae8bHq861o114T.jpg",
                      "options": [
                          {
                              "title": "안시성",
                              "isCorrect": false
                          },
                          {
                              "title": "화산고",
                              "isCorrect": false
                          },
                          {
                              "title": "클래식",
                              "isCorrect": false
                          },
                          {
                              "title": "비열한 거리",
                              "isCorrect": true
                          }
                      ]
                  },
                  {
                      "poster_path": "/dOVLy8K0hBFsxW2whcuTDPWrdlZ.jpg",
                      "options": [
                          {
                              "title": "똥파리",
                              "isCorrect": false
                          },
                          {
                              "title": "독전",
                              "isCorrect": true
                          },
                          {
                              "title": "살인자의 기억법",
                              "isCorrect": false
                          },
                          {
                              "title": "기억의 밤",
                              "isCorrect": false
                          }
                      ]
                  },
                  {
                      "poster_path": "/pJKy1yvnKh8UjcuYeG3Rt35xHFA.jpg",
                      "options": [
                          {
                              "title": "다른 나라에서",
                              "isCorrect": false
                          },
                          {
                              "title": "번 더 스테이지: 더 무비",
                              "isCorrect": true
                          },
                          {
                              "title": "터널",
                              "isCorrect": false
                          },
                          {
                              "title": "밀양",
                              "isCorrect": false
                          }
                      ]
                  },
                  {
                      "poster_path": "/x7O15z9hChNj3W1504Iv5kjUUWi.jpg",
                      "options": [
                          {
                              "title": "헨젤과 그레텔",
                              "isCorrect": false
                          },
                          {
                              "title": "싸이보그지만 괜찮아",
                              "isCorrect": true
                          },
                          {
                              "title": "고양이: 죽음을 보는 두개의 눈",
                              "isCorrect": false
                          },
                          {
                              "title": "82년생 김지영",
                              "isCorrect": false
                          }
                      ]
                  },
                  {
                      "poster_path": "/hUgPWAyJ3GOoIVctVJJ6yqyaIpW.jpg",
                      "options": [
                          {
                              "title": "국제시장",
                              "isCorrect": false
                          },
                          {
                              "title": "나의 PS 파트너",
                              "isCorrect": false
                          },
                          {
                              "title": "타워",
                              "isCorrect": false
                          },
                          {
                              "title": "어린 신부",
                              "isCorrect": true
                          }
                      ]
                  },
                  {
                      "poster_path": "/2MCy07o0FHQYjigKim5bHF78267.jpg",
                      "options": [
                          {
                              "title": "끝까지 간다",
                              "isCorrect": true
                          },
                          {
                              "title": "더 테러 라이브",
                              "isCorrect": false
                          },
                          {
                              "title": "도어락",
                              "isCorrect": false
                          },
                          {
                              "title": "끝까지 간다",
                              "isCorrect": false
                          }
                      ]
                  },
                  {
                      "poster_path": "/yXnGO8s2aWyYenZVMbuco1W5cQk.jpg",
                      "options": [
                          {
                              "title": "용서는 없다",
                              "isCorrect": false
                          },
                          {
                              "title": "숨바꼭질",
                              "isCorrect": false
                          },
                          {
                              "title": "관상",
                              "isCorrect": false
                          },
                          {
                              "title": "초능력자",
                              "isCorrect": true
                          }
                      ]
                  }
              ],
    

        }
    },

    methods:{
        startQuizFunc(){
            this.startQuiz = true
            this.countDownTimer()
        },
        handleAnswerClick(isCorrect){
            clearTimeout(this.timer);
            let nextQuestion = this.currentQuestion + 1;
            if(isCorrect){
                this.score = this.score + 1;
            }
            if(nextQuestion < this.questions.length){
            this.currentQuestion = nextQuestion;
            // this.$store.state.questionAttended = this.currentQuestion;
            // localStorage.setItem('qattended', this.currentQuestion)

            this.countDown = 10;
            this.countDownTimer();
            }
            else{
                // localStorage.removeItem('qattended')
                this.showScore = true;
                // localStorage.setItem('testComplete',this.showScore)
            }

        },
        countDownTimer() {
                if(this.countDown > 0) {
                    this.timer = setTimeout(() => {
                        this.countDown -= 1
                        this.countDownTimer()
                    }, 1000)
                }
                else{
                    this.handleAnswerClick(false)
                }
            }
    },
     created() {
        //  alert(this.$store.state.questionAttended)
        //    this.showScore = localStorage.getItem('testComplete') || false
        //    this.currentQuestion = localStorage.getItem('qattended') || 0
        //    this.countDownTimer()
        //    this.fetchQuiz()
        }
    
}
</script>

<style scoped>
.card {
    min-width: 100%;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 10px 10px 42px 0px rgba(0, 0, 0, 0.75);
}
.card-q{
    min-width: 60%;
}
.ans-option-btn{
    min-width: 50%;
    font-size: 16px;
    color: #ffffff;
    align-items: center;
    cursor: pointer;
    margin-bottom: 5px;


}
.answer-section {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.timer-text {
  background: rgb(230, 153, 12);
  padding: 15px;
  margin-top: 20px;
  margin-right: 20px;
  border: 5px solid rgb(255, 189, 67);
  border-radius: 15px;
  text-align: center;
}

.card-img, .card-img-top {
    border-top-left-radius: calc(0.25rem - 1px);
    border-top-right-radius: calc(0.25rem - 1px);
    height: 350px;
}

#poster-image {
  /* position: absolute; */
  height: 100px;
  width: 50%;
  background: no-repeat center center fixed;
  margin-top: 50px;
  background-position-y: -10%;
  overflow: hidden;
}

#question {
  margin-top: 100px;
}

</style>
