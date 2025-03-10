<template>
  <Content style="margin-top: 200px;  width: 500px;">
    <div class="row justify-content-md-center">
      <div class="col-3">
        <h2 class="text-center" style="font-size: 25px; font-weight: bold; margin-bottom: 50px;">登录</h2>
        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label for="username" class="form-label">用户名</label>
            <input v-model="username" type="text" class="form-control" id="username" required>
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">密码</label>
            <input v-model="password" type="password" class="form-control" id="password" required>
          </div>
          <div class="error-message">{{ error_message }}</div>
          <button type="submit" class="btn btn-primary">登录</button>
        </form>
      </div>
    </div>
  </Content>
</template>

<script>
import { mapActions } from 'vuex';
import Content from '../components/Content';

export default {
  name: 'Login',
  components: {
    Content,
  },
  data() {
    return {
      username: '',
      password: '',
      error_message: '',
    };
  },
  methods: {
    ...mapActions(['login']),
    handleLogin() {
      this.login({
        username: this.username,
        password: this.password,
        success: (response) => {
          if(response.data.code == -1){
            alert(response.data.msg)
          }
          // 登录成功后的其他操作，例如跳转到主页
          else
            this.$router.push('/');
        },
        error: () => {
          // 处理登录失败逻辑
          console.error('登录失败');
          // 显示错误消息
         
        },
      });
    },
  },
};
</script>

<style scoped>
/* 你的样式 */
</style>