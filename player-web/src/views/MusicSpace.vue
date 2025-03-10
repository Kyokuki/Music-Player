<template>
  <Content>
    <div class="row">
        <div class="col-3">
          <UserInfo :user="user" />
          <Upload :id="user.id"/>
        </div>
        <div class="col-9">
          <MusicList :list="music_list" :id="user.id"/>
        </div>
      </div>
  </Content>
</template>

<script>
  import Content from '../components/Content';
  import UserInfo from '../components/UserInfo';
  import MusicList from '../components/MusicList';
  import Upload from '../components/Upload';
  import { ref, watch } from 'vue';
  import { useStore } from 'vuex';
  export default {
    name: 'MusicSpace',
    components:{
      Content,
      UserInfo,
      MusicList,
      Upload,
    },
    data() {
      return {
        info: {
          fixed: false,       // 不开启吸底模式
          listFolded: true,   // 折叠歌曲列表
          autoplay: false,    // 开启自动播放
          preload: "none",    // 自动预加载歌曲
          loop: "all",        // 播放循环模式、all全部循环 one单曲循环 none只播放一次
          order: "list",      // 播放模式，list列表播放, random随机播放
        },
      };
    },
    setup() {
      const store = useStore();
      const user = ref(store.getters.user);
      const music_list = ref({
        musics:[]
      });
      music_list.value.musics = store.getters.music
      watch(
        () => store.getters.music,
        () => {
          music_list.value.musics = store.getters.music;
        }
      );
      return {user,music_list};
    }
  }
</script>

<style scoped>

</style>