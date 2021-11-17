<template>
  <nav class="navbar navbar-light bg light">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">(로고)</router-link>
      <div class="navbar">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/login" class="nav-link">(로그인)</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/signup" class="nav-link">(회원가입)</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/profile" class="nav-link">(프로필)</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/v404v" class="nav-link disabled">(404)</router-link>
          </li>
        </ul>
      </div>
    <form class="d-flex">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
}
</script>

<style>

</style>