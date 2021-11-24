import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    trendingMovieList: [],
    selectedMovie: '',
    myWishList: [],
    searchResults: [],
    
    selectedArticle: '',
    selectedArticleComments: [],
    popularByGenre: {},
    userProfile: '',
    userId: null,
    isLogin: false,
    token: null,
  },
  mutations: {
    MOVIE_DETAIL(state, trendingMovie) {
      state.selectedMovie = trendingMovie
      console.log(state.selectedMovieLiked)
    },
    CHANGE_LOGGED(state){
      state.isLogin = !state.isLogin
    },
    SET_JWT_TOKEN(state, token) {
      const base64Payload = token.split('.')[1]; 
      const payload = Buffer.from(base64Payload, 'base64'); 
      const result = JSON.parse(payload.toString())

      state.userId = result['user_id']
      
      state.token = token
    },
    SELECT_ARTICLE(state, article){
      state.selectedArticle = article
    },
    SET_COMMENTS(state, comments){
      state.selectedArticleComments = comments 
    },
    COMMENT_CREATED(state, comment){
      state.selectedArticleComments.unshift(comment)
    },
    EDIT_COMMENT(state, comment) {
      // console.log(state.selectedArticleComments)
      // console.log(comment)
      state.selectedArticleComments = state.selectedArticleComments.map((cmt) =>{
        if (cmt.id === comment.id) {
          return comment
        } else {
          return cmt
        }
      })
    },
    DELETE_COMMENT(state, commentId) {
      state.selectedArticleComments = state.selectedArticleComments.filter((cmt) => {
        return cmt.id !== commentId
      })
    },
    UPDATE_MOVIE_RATING(state, rating) {
      state.selectedMovie.ratings = state.selectedMovie.ratings.map((tmpRating) => {
        if (tmpRating.user === rating.user) {
          return rating
        } else {
          return tmpRating
        }
      })
      if (state.selectedMovie.ratings.every((tmp) => {
        return tmp.user !== rating.user
      })){
        state.selectedMovie.ratings.unshift(rating)
      }
    },
    DELETE_MOVIE_RATING(state, ratingId) {
      state.selectedMovie.ratings = state.selectedMovie.ratings.filter(rating => {
        return rating.id !== ratingId
      })
    },
    POPULAR_BY_GENRE(state, params){
      state.popularByGenre[params.genre] = params.data
    },
    MY_WISH_LIST(state, data){
      state.myWishList = data.wishlist
      // console.log(state.myWishList)
    },
    USER_PROFILE(state, data) {
      state.userProfile = data
    },
    SEARCH_MOVIE(state, data) {
      state.searchResults = data
    }
  },
  actions: {
    movieDetail({ commit }, trendingMovie) {
      commit('MOVIE_DETAIL', trendingMovie)
    },
    changeLogged({ commit }){
      commit('CHANGE_LOGGED')
    },
    setJwtToken({ commit }, token){
      commit('SET_JWT_TOKEN', token)
    },
    selectArticle({ commit }, article){
      commit('SELECT_ARTICLE', article)
    },
    setComments({ commit }, comments){
      commit('SET_COMMENTS', comments)
    },
    commentCreated({ commit }, comment){
      commit('COMMENT_CREATED', comment)
    },
    editComment({ commit }, comment) {
      commit('EDIT_COMMENT', comment)
    },
    deleteComment({ commit }, commentId) {
      commit('DELETE_COMMENT', commentId)
    },
    updateMovieRating({ commit }, rating) {
      commit('UPDATE_MOVIE_RATING', rating)
    },

    popularByGenre({ commit }) {
      // const API_KEY = process.env.VUE_APP_API_KEY
      const genres = [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770]
      genres.forEach((genre) => {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/genre-popular/${genre}/`,
      })
        .then((res) => {
          commit('POPULAR_BY_GENRE', {
            genre: genre,
            data: res.data
          })
        })
        .catch((err) => {
          console.log(err)
        })
      })
    },
    deleteMovieRating({ commit }, ratingId) {
      commit('DELETE_MOVIE_RATING', ratingId)
    },

    myWishList({ commit }, data){
      commit('MY_WISH_LIST', data)
    },
    userProfile({ commit }, data) {
      commit('USER_PROFILE', data)
    },
    searchMovie({ commit }, data) {
      commit('SEARCH_MOVIE', data)
    }
  },
  modules: {
  }
})
