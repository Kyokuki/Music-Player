<template>
  <NavBar/>
  <router-view/>
  <div id="aplayer"></div>
</template>
<script>
import NavBar from './components/NavBar';
import { useStore } from 'vuex';
import {onMounted,watch, ref} from 'vue';
import APlayer from "aplayer"; // 引入音乐插件
import "aplayer/dist/APlayer.min.css"; // 引入音乐插件的样式
import { getMusic } from '@/api';
export default{
  name:'App',
  components:{
    NavBar,
  },
  setup() {
    const store = useStore();
    const updateMusic = (music) => {
      store.dispatch('updateMusic', music);
    };
    const updateAplayer = (ap) => {
      store.dispatch('updatePlayer', ap);
    };
    let aplayer = ref(null);
    watch(
        () => store.getters.isLoggedIn,
        () => {
          fetchList();
        }
      );
    const fetchList = async () => {
      if(!store.getters.isLoggedIn)
        return;
      try{
        const response = await getMusic(store.getters.user.id);
        updateMusic(response.data);
        aplayer.value = ref(new APlayer({
          container: document.getElementById("aplayer"),
          audio: response.data, // 音乐信息
          fixed: false, // 不开启吸底模式
          listFolded: true, // 折叠歌曲列表
          autoplay: false, // 开启自动播放
          preload: "auto", // 自动预加载歌曲
          loop: "all", // 播放循环模式、all全部循环 one单曲循环 none只播放一次
          order: "list", //  播放模式，list列表播放, random随机播放
        }));
        updateAplayer(aplayer)
      }catch(error){
        console.error('Error fetching data:', error);
      }
    };
    onMounted(()=>{
      fetchList();
    });
    return {aplayer};
  }
}
</script>

<style scoped>
#aplayer {
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 9999;
}
</style>
