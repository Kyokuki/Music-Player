import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue';
import MusicSpace from '../views/MusicSpace.vue';
import Register from '../views/Register.vue';
import NotFound from '../views/NotFound.vue';
import Discover from '../views/Discover.vue';
import store from '../store';
import Home from '../views/Home.vue';
const routes = [
  {
    path: '/musicspace/',
    name: 'musicspace',
    component:MusicSpace,
    meta: { requiresAuth: true },
  },
  {
    path: '/discover/',
    name: 'discover',
    component:Discover,
  },
  {
    path: '/',
    name: 'home',
    component:Home
  },
  {
    path: '/login/',
    name: 'login',
    component:Login
  },
  {
    path: '/register/',
    name: 'register',
    component:Register
  },
  {
    path: '/404/',
    name: '404',
    component:NotFound
  },
  {
    path: '/:catchAll(.*)',
    redirect: "/404/"
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isLoggedIn) {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
});
export default router
