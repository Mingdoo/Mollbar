<template>
  <div>
    {{ selectedMovie.title }}

  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  data: function() {
    return {
      selectedMovie: this.$store.state.selectedMovie
    }
  }
}
</script>

<style>

</style>