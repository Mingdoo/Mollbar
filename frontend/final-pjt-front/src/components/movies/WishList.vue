<template>
  <div class="container-carousel row" style="min-height: 0;">
    <div class="col-1" @click="clickLeft" style="cursor:pointer;">
      <i class="fa fa-chevron-left" aria-hidden="true" style="font-size: 40px;"></i>
    </div>
    <div class="col-10 carousel" style="width: 83.33333333%;">
        <wish-list-item
          v-for="wishMovieId in wishList"
          :key="wishMovieId"
          :wish-movie-id="wishMovieId"
        >
        </wish-list-item>
    </div>
    <div class="col-1" @click="clickRight" style="cursor:pointer;">
      <i class="fa fa-chevron-right" aria-hidden="true" style="font-size: 40px;"></i>
    </div>
  </div>
</template>

<script>
import WishListItem from '@/components/movies/WishListItem';
import $ from 'jquery'

export default {
  name: "WishList",
  components: {
    WishListItem
  },
  data() {
    return {
      scrollAmount: 0,
      scrollPerclick: 200
    }
  },
  computed: {
    wishList() {
      return this.$store.state.myWishList
    }
  },
  methods: {
    clickLeft() {
      console.log('left')
      $(".carousel").animate({
          scrollLeft: (this.scrollAmount -= this.scrollPerclick)
        }, 400);
      this.scrollAmount -= this.scrollPerclick
    },
    clickRight() {
      console.log('right')
      const sliders = document.querySelector(".carousel")
      console.log(sliders)
      this.scrollAmount += this.scrollPerclick
      if (this.scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        $(".carousel").animate({
          scrollLeft: (this.scrollAmount += this.scrollPerclick)
          }, 400);
        }
    }
  },
}
</script>

<style>
.container-carousel {
  align-content: flex-start;
}

.wishlist {
  width: 83.33333333%;
}

.container-carousel .switchLeft,
.container-carousel .switchRight {
  color: rgb(255, 255, 255);
  font-weight: bold;
  text-decoration: none;
  height: 300px;
  width: 40px;
  font-size: 30px;
  text-align: center;
  background-color: lightgray;
  font-family: sans-serif;
  z-index: 3;
  position: relative;
}
.sliderButton {
  display: inline-block;
}

.container-carousel .switchLeft{
  position: relative;
  left: -10px;
}

.container-carousel .switchRight{
  position: relative;
  right: -10px;
}
</style>