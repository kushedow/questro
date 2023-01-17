<script setup>

import QuestionsPage from './components/QuestionsPage.vue'
import MainMenuPage from './components/MainMenuPage.vue'
import { ref } from 'vue'

</script>

<template lang="pug">
.main-container
  .status.text-center
    span.badge.bg-success(v-if="is_connected") online
    span.badge.bg-danger(v-else) offline
  RouterView
  footer.text-center


</template>

<script>

import {io} from "socket.io-client";

const count = ref(0)

export default {

  methods: {

    // обновяем код
    setCode(code_v){
      this.code = code_v
    },

    // обновляем игрока
    setPlayers(players_v) {     // меняем код подключения
      this.players = players_v
      this.$forceUpdate()
    },

    startRound(){

      

    }

  },

  data() {
    return {

      socket: {},  // объект доступа к сокету
      code : "____",   // код присоединения к игре
      is_connected: false, // подсоединен ли соект
      players: [], // список игроков в нашей группе

      questions: [],
    }
  },

  mounted(){

    // создаем прокси для методов
    const self = this

    // Создаем сокет
    this.socket = io("ws://0.0.0.0:5001/");

    // Присоединились
    this.socket.on("connect", () => {

      this.is_connected = true
      this.socket.emit("server/create_game", {})

      console.log("APP: SOCKET connected")
    });

    // Отсоединились
    this.socket.on("disconnect", () => {
      this.is_connected = false
      console.log("APP: SOCKET disconnected")
    });

    // Вызвали ошибку client/exception
    this.socket.on('client/exception', function (received_data) {

      alert(received_data.error)

    });

    // Обрабатываем ответ с игрой от сервера
    this.socket.on('client/game_updated', function (received_data) {

      // запоминаем код и игроков
      self.setCode(received_data.code)
      self.setPlayers(received_data.players)

      console.log("APP:client/game_updated")
      console.log(received_data)

      self.$forceUpdate();

    });


  },

}

</script>

<style>

    body {
      background-color: #222;
    }

    .main-container {
      background-color: #eee;
      width: 420px;
      padding: 16px;
      margin: 2rem auto 2rem;
      border: 1px solid #eee;
      border-radius: 8px;
    }

</style>
