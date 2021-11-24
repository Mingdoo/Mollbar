<template>
  <div class="container mt-5 mb-3">
    <div class="row container-fluid mt-5">
      <search-list v-for="searchResult in searchResults" :key="searchResult.id" :search-result="searchResult"></search-list>
    </div>
  </div>
</template>

<script>
import SearchList from '@/components/movies/SearchList'

export default {
  name: "Search",
  components: {
    SearchList
  },
  computed: {
    searchResults() {
      return this.$store.state.searchResults
    }
  }
}
</script>

<style>

</style>