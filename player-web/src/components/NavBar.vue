<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <router-link class="nav-link" :to="{name:'home'}">
      <img src="../assets/audio256.png" alt="Logo" width="35" height="35" >
      <span style="font-size: 25px; font-weight: bold; margin-left: 10px;">在线音乐</span>
    </router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarText" style="margin-left: 20px;">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'musicspace'}">创作空间</router-link>
        </li>
     
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'discover'}">发现音乐</router-link>
        </li>
      </ul>

      <!-- <form @submit.prevent="search">
        <img src="../assets/search.png" alt="Search" width="35" height="35">
        <el-input v-model="input" style="width: 240px" placeholder="搜索音乐"/> 
      </form> -->
    </div>


    <div class="collapse navbar-collapse" id="navbarText">
      <ul class="navbar-nav" v-if="!store.getters.isLoggedIn">
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'login'}">登录</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{name:'register'}">注册</router-link>
        </li>
      </ul>

      <ul class="navbar-nav" v-else>
        <li class="nav-item">
          <a class="nav-link" style="cursor: pointer" @click="handleLogout">退出</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
import { useStore } from 'vuex';
import { mapActions } from 'vuex';
export default{
  name:'NavBar',
  setup() {
    const store = useStore();
    return {store};
  },
  methods: {
    ...mapActions(['logout']),
    handleLogout() {
      this.logout();
      this.$router.push('/login/');
    },
    search() {
      // 执行搜索逻辑，处理查询字符串
      // ...
      // 跳转到搜索结果页面或执行其他操作
    }
  },
  data() {
    return {
      iconUrl: require('@/assets/search.png'),
      query: ''
    }
  },
}
</script>

<style scoped>
.navbar-collapse {
  display: flex;
  justify-content: flex-end;
}
</style>