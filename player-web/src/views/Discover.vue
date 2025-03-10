<template>
  <div class="card list">
    <div class="card-body">
      <div class="scrollable-container">
        <div v-for="music in musicData" :key="index">
          <div class="card music">
            <div class="card-body">
              <div class="row">
                <div class="col-10 music_name">{{ music.name }}</div>
                <div class="col-2 artist">歌手：{{ music.artist }}</div>
              </div>
            </div>
          </div>
      </div>  
      </div>
    </div>
  </div>
</template>

<script>
  import Content from '../components/Content';
  import {ref, watch } from 'vue';
  import { useStore } from 'vuex';
  import { discover } from '@/api';
  import axios from 'axios';
  export default {
    name: 'Discover',
    components:{
      Content,
    },
    setup(props) {
      const musicData = ref([]);
      (async () => {
        try {
          const response = await discover();  // 调用 discover 函数获取歌曲信息
          musicData.value = response.data;    // 假设响应数据是一个包含歌曲信息的对象或数组
          console.log(musicData);             // 输出歌曲信息
        } catch (error) {
          console.error(error); // 处理错误
        }
      })();
      return {musicData};
    }
}
</script>

<style scoped>

</style>
