<template>
    <div class="card upload-music">
        <div class="card-body">
            <div class="mb-3">
              <label for="formFileMultiple" class="form-label">上传音乐</label>
              <input class="form-control" type="file" id="formFile" @change="handleFileChange">
              <button type="button" class="btn btn-primary btn-sm" @click="uploadFiles">上传</button>
            </div>
        </div>
    </div>
</template>

<script>
import { postMusic } from '@/api';

export default {
  name: 'Upload',
  props:{
    id:{
      type:Object,
      required:true
    },
  },
  data() {
    return {
      files: [] // 用于存储选择的文件
    };
  },
  methods: {
    handleFileChange(event) {
      // 当文件选择改变时，更新文件列表
      this.files = Array.from(event.target.files);
    },
    uploadFiles() {
      if (this.files.length > 0) {
        // 创建一个FormData对象，用于发送文件
        const formData = new FormData();
        this.files.forEach(file => {
          const isLt20M = file.size / 1024 /1024 <20;
          if (!isLt20M) {
            alert('上传的文件大小不能超过20MB!')
            return;
          }
          const fileType = file.type;
          if (fileType !== 'audio/mpeg') {
            alert('只能上传MP3文件!');
            return;
          }
          formData.append('file', file);
        });

        // 使用axios发送文件
        postMusic(formData,this.id).then(response => {
          console.log('文件上传成功', response);
          // 重置文件列表
          window.location.reload();
        }).catch(error => {
          console.error('文件上传失败', error);
        });
      }
    }
  }
};
</script>

<style scoped>
.upload-music {
    margin-top: 20px;
}
button {
    margin-top: 10px;
}
</style>