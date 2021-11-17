import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    trendingMovieList: [],
    selectedMovie: '',
  },
  mutations: {
    MOVIE_DETAIL(state, trendingMovie) {
      state.selectedMovie = trendingMovie
    }
  },
  actions: {
    movieDetail({ commit }, trendingMovie) {
      commit('MOVIE_DETAIL', trendingMovie)
    }
  },
  modules: {
  }
})
