<template>
  <Content style="margin-top: 200px;  width: 500px;">
    <div class="row justify-content-md-center">
      <div class="col-3">
        <h2 class="text-center" style="font-size: 25px; font-weight: bold; margin-bottom: 50px;">注册</h2>
        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="username" class="form-label">用户名</label>
            <input v-model="username" type="text" class="form-control" id="username">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">密码</label>
            <input v-model="password" type="password" class="form-control" id="password">
          </div>
          <button type="submit" class="btn btn-primary">注册</button>
        </form>
      </div>
    </div>
  </Content>
</template>

<script>
  import { postRegister } from '@/api';
  import Content from '../components/Content';
  export default {
    name: 'Register',
    components:{
      Content
    },
    data() {
      return {
        username: "",
        password: ""
      }
    },
    methods: {
      submit() {
        postRegister(this.username,this.password)
        .then((response) => {
            alert(response.data.msg)
        }).catch(error => {
          console.error('注册失败', error);
        });
      }
    }
  }
</script>

<style scoped>

</style>