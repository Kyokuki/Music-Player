import Vue from 'vue'
import axios from 'axios'

export const getMusic = (id) => {return axios.get('http://localhost:8000/api/music/',{
    params: {
      userid: id
    }
  });
}

export const discover = () => {return axios.get('http://localhost:8000/api/discover/',{

});
}

export const postImage = (formData,id) => {
  formData.append('userid', id);
  return axios.post('http://localhost:8000/api/uploadimage/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
}
export const postMusic = (formData,id) => {
  formData.append('userid', id);
  return axios.post('http://localhost:8000/api/uploadmusic/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
}

export const postLogin = (username,password) => {
  return axios.post('http://localhost:8000/api/user/login/', {
    username,
    password,
  });
}

export const postRegister = (username,password) => {
  return axios.post('http://localhost:8000/api/user/register/', {
    "username": username, 
    "password": password
  });   
}

export const postDelete = (userid,musicid) => {
  console.log(userid);
  console.log(userid);
  return axios.post('http://localhost:8000/api/deletemusic/', {
    "userid": userid, 
    "musicid": musicid
  });
}