<template>
  <footer class="row py-2 mt-5 border-top">
    <div class="col-3 offset-1 d-flex align-items-center">
      <!-- <a href="/" class="d-flex align-items-center mb-3 link-dark text-decoration-none">
        <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
      </a> -->
      <p class="text-muted">&copy; Mollbar Inc. 2021</p>
    </div>

    <div class="col-4">
      <img src="../assets/tv_with_mollbar_3.png" alt="" id="footer-image">
    </div>

    <div class="col-3 d-flex justify-content-end align-items-center">
      <a href="https://github.com/Mingdoo/Mollbar" class="text-decoration-none">
        <i class="fab fa-github" id="github-icon"></i>
      </a>
    </div>
  </footer>
</template>

<script>
export default {

}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);

footer {
  font-family: 'Noto Sans KR', sans-serif;
  background-color: #EDEDED;
}

.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

#github-icon {
  color: #2c3e50;
  font-size: 2.5rem;
}

#github-icon:hover {
  color: black;
}

#ssafy-link {
  margin-left: 10px;
}

#footer-image {
  height: 270px;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}
</style>