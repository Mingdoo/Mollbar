import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import NotFound from '@/pages/NotFound';
import Profile from '@/pages/Profile'
import Login from '@/components/accounts/Login';
import MovieDetail from '@/pages/MovieDetail';
import SignUp from '@/components/accounts/SignUp';
import CommunityHome from '@/pages/CommunityHome'

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
    path: '/detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/community/',
    name: 'CommunityHome',
    component: CommunityHome
  },
  { path: "*", component: NotFound }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
