<template>
  <div class="container">
    <table class="table text-white table-dark">
      <thead class="">
        <th scope="col">게시글 번호</th>
        <th scope="col">제목</th>
        <th scope="col">작성자</th>
        <th scope="col">게시일</th>
        <th scope="col">최근 업데이트</th>
      </thead>
      <tbody>
        <article-card
        v-for="article in articles"
        :key="article.id"
        :article="article"
        class="articlecard mx-1"
        >
        </article-card>
      </tbody>
    </table>
    <button class="btn btn-secondary mt-5 w-75 h-100" @click="createArticle">새로운 글 작성하기</button>
  </div>
</template>

<script>
import ArticleCard from '@/components/community/ArticleCard';
export default {
  name: "ArticleList",
  props: {
    articles: Array,
  },
  components: {
    ArticleCard,
  },
  methods: {
    createArticle() {
      if (localStorage.getItem('jwt')){
        this.$router.push({ name: "ArticleCreationForm", params: { article: ''}})  
      }
    }
  }
}
</script>

<style>
/* .articlecard {
  background-color:palegoldenrod;
} */

</style>