// store/index.js
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { postLogin } from '@/api';



export default new Vuex.Store({
  state: {
    user: localStorage.getItem('user') != "undefined" ? JSON.parse(localStorage.getItem('user')) : null,
    music: [],
    ap: null
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
      localStorage.setItem('user', JSON.stringify(user));
    },
    CLEAR_USER(state) {
      state.user = null;
      localStorage.removeItem('user');
    },
    UPDATE_MUSIC(state,music){
      state.music = music;
      state.user.music_nums = music.length
    },
    UPDATE_APLAYER(state,ap){
      state.ap = ap;
    },
    UPDATE_USER_PHOTO(state, photoUrl) {
      state.user.photo = photoUrl;
      localStorage.setItem('user', JSON.stringify(state.user));
    },
  },
  actions: {
    async login({ commit }, { username, password, success, error }) {
      try {
        const response = await postLogin(username,password);
        const user = response.data.userinfo;
        commit('SET_USER', user);
        success(response);
      } catch (err) {
        error();
      }
    },
    logout({ commit }) {
      commit('CLEAR_USER');
      window.location.reload();
    },
    updateUserPhoto({ commit }, photoUrl) {
      commit('UPDATE_USER_PHOTO', photoUrl);
    },
    updateMusic({ commit }, music) {
      commit('UPDATE_MUSIC', music);
    },
    updatePlayer({ commit }, ap) {
      commit('UPDATE_APLAYER', ap);
    },
  },
  getters: {
    isLoggedIn: state => !!state.user,
    user: state => state.user,
    music: state => state.music,
    aplayer: state => state.ap
  },
});