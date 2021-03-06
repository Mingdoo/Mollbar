import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import NotFound from '@/pages/NotFound';
import Profile from '@/pages/Profile'
import Login from '@/components/accounts/Login';
import MovieDetail from '@/pages/MovieDetail';
import SignUp from '@/components/accounts/SignUp';
import CommunityHome from '@/pages/CommunityHome'
import ArticleCreationForm from '@/components/community/ArticleCreationForm';
import ArticleDetail from '@/pages/ArticleDetail';
import Quiz from '@/pages/Quiz';
import Search from '@/pages/Search';

Vue.use(VueRouter)

const routes = [
  // home
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  // accounts
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },

  // movies
  {
    path: '/movies/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/quiz',
    name: 'Quiz',
    component: Quiz
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },

  //community
  {
    path: '/community',
    name: 'CommunityHome',
    component: CommunityHome
  },
  {
    path: '/community/create',
    name: 'ArticleCreationForm',
    component: ArticleCreationForm
  },
  {
    path: '/community/:article_id',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  { path: "*", component: NotFound }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
