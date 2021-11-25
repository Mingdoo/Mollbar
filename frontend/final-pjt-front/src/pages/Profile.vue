<template>
  <section>
    <!-- <div class="container"> -->
      <div class="row">
        <!-- 1. 프로필 부분 -->
        <div class="col-4 profile-area row">
          <b-card
            bg-variant="light"
            border-variant="danger"
            tag="article"
            style="max-width: 20rem; margin: 0px auto; border: solid 3px #ff0000; border-bottom: solid 3px #ff0000;"
            class="mb-2 d-flex flex-column justify-content-between col-8 offset-2"
          >
            <div class="d-flex flex-column justify-content-between pt-3 pb-3" style="height: 100%;">
              <!-- 1-1 기본 정보 -->
              <div>
                <div>
                  <img src="https://picsum.photos/200" id="profile-image">
                </div>
                <div class="vertical-line h4 mt-3 mb-3">{{ userProfile.username }}</div>
                <p>{{ userProfile.email }}</p>
                <p>가입한 지 <span class="red ">{{ userProfile.days_since_joined }}</span>일 째</p>
              </div>
              <!-- 1-2. 회원 탈퇴 / 비밀번호 변경 -->
              <div style="width: 100%;">
                <b-button class="profile-btn" style="background-color: #444444;" @click="changePassword">
                  비밀번호 변경
                </b-button>

                <b-button id="toggle-btn" class="profile-btn" style="background-color: #DA0037;" @click="toggleModal">회원 탈퇴</b-button>

                <b-modal ref="my-modal" hide-footer hide-header title="마지막으로 한번만 붙잡을게요..." class="noto">
                  <div class="d-block text-center align-center">
                    <p class="mt-3 noto">회원 탈퇴시</p>
                    <p class="mt-3 noto">그동안 남겨주신 글/댓글/평점/찜 목록 등이 모두 삭제됩니다.</p>
                    <p class="mt-3 noto">그래도 탈퇴하시겠습니까? </p>
                  </div>
                  <div class="d-block text-center pt-3">
                    <b-button style="background-color: #444444;" class="me-5 modal-btn" @click="toggleModal">
                      아니오
                    </b-button>
                    <b-button style="background-color: #DA0037;" block @click="signOut" class="modal-btn signout">
                      네 (피도 눈물도 없이 탈퇴하기)
                    </b-button>
                  </div>
                </b-modal>
              </div>
              <!-- 1-3. tv with mollbar 이미지 -->
              <div>
                <img src="../assets/tv_with_mollbar.png" alt="" id="mollbar-image">
                <!-- <img src="https://media.vlpt.us/images/ready2start/post/db891b0e-9a28-4b40-9cf8-7fc58fe3e0b9/tv_with_mollbar.png" alt="" id="mollbar-image"> -->
              </div>
            </div>
            

          </b-card>
        </div>

        <!-- 2. 영화 부분 -->
        <div class="col-8 movie-area">
          <div class="container-carousel row">
            <h2 class="np" style="cursor:pointer;">
              내가 찜한 영화
            </h2>
            <div class="col-1" @click="clickLeft" style="cursor:pointer;">
              <i class="fa fa-chevron-left" aria-hidden="true" style="font-size: 40px;"></i>
            </div>
            <div class="carousel col-10">
              <wish-list-item
                v-for="wishListId in userProfile.wishlist"
                :key="wishListId"
                :wish-list-id="wishListId"
              >
              </wish-list-item>
            </div>
            <div class="col-1" @click="clickRight" style="cursor:pointer;">
              <i class="fa fa-chevron-right" aria-hidden="true" style="font-size: 40px;"></i>
            </div>
          </div>
          <p>
            찜한 목록 : {{ userProfile.wishlist }}

            평가 목록 : {{ userProfile.rating_set }}
          </p>
        </div>

      </div>
    <!-- </div> -->
  </section>
</template>

<script>
import Swal from 'sweetalert2'
import $ from 'jquery'; 
import WishListItem from '@/components/movies/WishListItem'
import axios from 'axios'

export default {
  name: "Profile",
  data() {
    return {
      scrollAmount: 0,
      scrollPerclick: 200,
      modalShow: false,
    }
  },
  components: {
    WishListItem,
  },
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
  },
  methods: {
    clickLeft() {
      $(`#carousel${this.genre}`).animate({
          scrollLeft: (this.scrollAmount -= this.scrollPerclick)
        }, 400);
      this.scrollAmount -= this.scrollPerclick
    },
    clickRight() {
      const sliders = document.querySelector(`#carousel${this.genre}`)
      this.scrollAmount += this.scrollPerclick
      if (this.scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        $(`#carousel${this.genre}`).animate({
          scrollLeft: (this.scrollAmount += this.scrollPerclick)
          }, 400);
        }
    },
    toggleModal() {
      this.$refs['my-modal'].toggle('#toggle-btn')
    },
    changePassword() {
      // TODO: 비밀번호 변경 (시간 없을 시 제외)
    },
    signOut() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'delete',
        url: 'http://127.0.0.1:8000/api/v1/accounts/signout/',
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(res => {
          localStorage.removeItem('jwt')
          this.$store.dispatch('changeLogged')
          this.$router.push({name: 'Login'})
          Swal.fire({
            position: 'top',
            icon: 'success',
            title: '회원 탈퇴가 완료되었습니다.',
            showConfirmButton: false,
            timer: 1500
          })
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);

body {
  margin: 0;
  font-family: 'Noto Sans KR', sans-serif;
  /* color: #444444; */
}

.noto {
  font-family: 'Noto Sans KR', sans-serif;
}

.h4 {
  font-size: 1.25rem;
  font-weight: bold;
}

.row {
  min-height: 80vh;
  margin-top: 2.5vh;
  margin-bottom: 2.5vh;
}

.profile-area {
  background-color: black;
  overflow: hidden;
}

#profile-image {
  width: 100px;
  height: 100px;
  border-radius: 70%;
}

.profile-btn {
  width: 80%;
  margin: 10px auto;
  border: none;
}

.profile-btn:hover {
  transform: scale(1.15);
}

.modal-btn {
  border: none;
}

.modal-btn:hover {
  transform: scale(0.9);
}

#mollbar-image {
  width: 200px;
  /* height: 200px; */
}

.movie-area {
  background-color: #EDEDED;
}

.vertical-line {
  border-left: 3px solid #ff0000;
}

.white {
  color: #EDEDED;
}

.red {
  color: #ff0000;
}

.gray {
  color: #444444;
}
</style>