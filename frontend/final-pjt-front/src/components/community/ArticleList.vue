<template>
  <div>
    <h5>Article List</h5>
    <!-- {{ articles }} -->
    <article-card
    v-for="article in articles"
    :key="article.id"
    :article="article"
    class="articlecard"
    >
    </article-card>
    <button class="btn btn-primary" @click="createArticle">Create</button>
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
    ArticleCard
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
.articlecard {
  background-color: darkslateblue;
}

</style>