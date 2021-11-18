import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    trendingMovieList: [],
    selectedMovie: '',
    isLogin: false,
  },
  mutations: {
    MOVIE_DETAIL(state, trendingMovie) {
      state.selectedMovie = trendingMovie
    },
    CHANGE_LOGGED(state){
      state.isLogin = !state.isLogin
    }
  },
  actions: {
    movieDetail({ commit }, trendingMovie) {
      commit('MOVIE_DETAIL', trendingMovie)
    },
    changeLogged({ commit }){
      commit('CHANGE_LOGGED')
    }
  },
  modules: {
  }
})
