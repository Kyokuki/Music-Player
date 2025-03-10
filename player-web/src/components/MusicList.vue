<template>
  <div class="card list">
    <div class="card-body">
      <div class="scrollable-container">
        <div v-for="(music, index) in list.musics" :key="index" @click="handleCardClick(index)">
          <div class="card music">
            <div class="card-body">
              <div class="row">
                <div class="col-10 music_name">{{ music.name }}</div>
                <div class="col-2 artist">歌手：{{ music.artist }}</div>
              </div>
            </div>
            <button class="delete-button" @click.stop="handleDelete(index)">删除</button>
          </div>
      </div>  
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex';
import {ref, watch } from 'vue';
import { postDelete } from '@/api';
  export default{
    name:"MusicList",
    props:{
      list:{
        type:Object,
        required:true
      },
      id:{
        type:Object,
        required:true
      },
    },
    watch: {
    // 监听 musicList prop 的变化
      list: {},
    },
    setup(props){
      const store = useStore();
      let ap = ref(store.getters.aplayer);
      watch(
        () => store.getters.aplayer,
        () => {
          ap= ref(store.getters.aplayer);
        }
      );
      const handleCardClick = (index) => {
        console.log(ap)
        ap.value.pause()
        ap.value.list.switch(index);
        ap.value.play();
      }
      const handleDelete = (index) => {
        //ap.value.list.remove(index);
        //props.list.musics.splice(index, 1);
        postDelete(props.id,props.list.musics[index].id);
        window.location.reload();
      };
      return {ap,handleCardClick,handleDelete};
    },
  }
</script>

<style scoped>
.singer {
    font-size: 14px;
    color: gray;
}  
.scrollable-container {
  height: 620px;
  overflow: auto;
}
.music {
  margin-top: 10px;
  cursor: pointer;
}
.music:hover {
  box-shadow: 2px 2px 10px lightgray;
  transition: 300ms;
}
</style>