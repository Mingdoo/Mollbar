<template>
  <div>
    <h1>Community</h1>
    <article-list :articles="articles"></article-list>
  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList';
import axios from 'axios';
const API_COMMUNITY_URL = "http://localhost:8000/api/v1/community/"

export default {
  name: "CommunityHome",
  components: {
    ArticleList,
  },
  data() {
    return {
      articles: null,
    }
  },
  methods: {
    },
  created() {
    const token = localStorage.getItem('jwt')
    axios({
      method: 'get',
      url: API_COMMUNITY_URL,
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then((res) => {
        console.log(res.data)
        this.articles = res.data
      })
      .catch(err => {
        alert(err)
      })
  },
  computed: {}
}
</script>

<style>

</style>