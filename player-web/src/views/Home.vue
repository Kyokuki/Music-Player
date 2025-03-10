<!-- <template>
  <div style="margin-top: 20px; margin-bottom: 20px; margin-left: 10px;">
    <span style="font-size: 50px; font-weight: bold; margin-top: 100px; margin-bottom: 20px; margin-left: 100px;">音乐推荐</span>
  </div>

  <div class="block text-center" style="margin-top: 30px; margin-bottom: 20px; margin-left: 100px; margin-right: 100px;">
    <el-carousel :interval="4000" type="card" height="400px" width="800px">
      <el-carousel-item v-for="item in images" :key="item.id">
        <img :src="item.imageUrl" alt="Image" width="800" height="400">
        <div class="image-overlay"></div>
        <p class="carousel-text">{{ item.caption }}</p>
      </el-carousel-item>
    </el-carousel>
  </div>
  
</template>

<script>
export default {
  data(){
    return {
      images: [
        { id: 1, imageUrl: require('@/assets/1.jpg'), caption: "Hello" },
        { id: 2, imageUrl: require('@/assets/2.jpg'), caption: "Hello" },
        { id: 3, imageUrl: require('@/assets/3.jpg'), caption: "Hello" },
        { id: 4, imageUrl: require('@/assets/4.jpg'), caption: "Hello" },
      ],
    };
  },
}

</script>

<style scoped>
.demonstration {
  color: var(--el-text-color-secondary);
}
.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 120px;
  background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%);
  filter: blur(10px);
}
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 400px;
  width : 800px;
  margin: 0;
  text-align: center;
  background-color: #99a9bf;
}
.carousel-text {
  position: absolute;
  bottom: 20px;
  left: 10%;
  transform: translateX(-50%);
  color: white;
  font-weight: bold;
  font-size: 22px;
  text-align: left;
}
</style> -->

<template>
  <div style="margin-top: 20px; margin-bottom: 20px; margin-left: 10px;">
    <span style="font-size: 50px; font-weight: bold; margin-top: 100px; margin-bottom: 20px; margin-left: 100px;">音乐推荐</span>
  </div>

  <div class="block text-center" style="margin-top: 30px; margin-bottom: 20px; margin-left: 100px; margin-right: 100px;">
    <el-carousel :interval="4000" type="card" height="400px" width="800px">
      <el-carousel-item v-for="item in audio" :key="index" @click="handleCardClick(item.id)">
      <!-- <el-carousel-item v-for="item in audio" :key="index"> -->
        <!-- <audio :src="item.url" controls></audio> -->
        <!-- <audio :src="item.url" controls class="carousel-audio"></audio> -->
        <img :src="item.cover" alt="Image" width="800" height="400">
        
        <div class="image-overlay"></div>
        
        <p class="carousel-text">{{ item.name }}</p>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
import { useStore } from 'vuex';
import { ref, watch, onMounted } from 'vue';
import APlayer from 'aplayer';

export default {
  name: "Home",
  data(){
    return {
      audio: [
        { id: 0, name: "October - Who's Lovin' You", artist: "October", url: require('@/assets/October - Who\'s Lovin\' You.mp3'), cover: require('@/assets/1.jpg') },
        { id: 1, name: "July - In Love", artist: "July", url: require('@/assets/July - In Love.mp3'), cover: require('@/assets/2.jpg') },
        { id: 2, name: "iris - Letter", artist: "iris", url: require('@/assets/iris - Letter.mp3'), cover: require('@/assets/3.jpg') },
        { id: 3, name: "Dennis Kuo - Track in Time", artist: "Dennis Kuo", url: require('@/assets/Dennis Kuo - Track in Time.mp3'), cover: require('@/assets/4.jpg') },
      ],
    };
  },
  props: {
    list: {
      type: Object,
      required: true
    },
    id: {
      type: Object,
      required: true
    },
  },
  watch: {
    list: {},
  },
  setup(props) {
    const store = useStore();
    let ap = ref(null);

    const handleCardClick = (index) => {
      ap.value.pause();
      ap.value.list.switch(index);
      ap.value.play();
    };

    onMounted(() => {
      ap.value = new APlayer({
        container: document.createElement('div'),
        audio: [
          { name: "October - Who's Lovin' You", artist: "October", url: require('@/assets/October - Who\'s Lovin\' You.mp3'), cover: require('@/assets/1.jpg') },
          { name: "July - In Love", artist: "July", url: require('@/assets/July - In Love.mp3'), cover: require('@/assets/2.jpg') },
          { name: "iris - Letter", artist: "iris", url: require('@/assets/iris - Letter.mp3'), cover: require('@/assets/3.jpg') },
          { name: "Dennis Kuo - Track in Time", artist: "Dennis Kuo", url: require('@/assets/Dennis Kuo - Track in Time.mp3'), cover: require('@/assets/4.jpg') },
        ]
      });
    });

    return { ap, handleCardClick };
  },
}
</script>

<style scoped>
.demonstration {
  color: var(--el-text-color-secondary);
}
.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 120px;
  background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%);
  filter: blur(10px);
}
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 400px;
  width: 800px;
  margin: 0;
  text-align: center;
  background-color: #99a9bf;
}
.carousel-text {
  position: absolute;
  bottom: 20px;
  left: 30%;
  transform: translateX(-50%);
  color: white;
  font-weight: bold;
  font-size: 22px;
  text-align: left;
}
</style>