<script setup>

import QuestionsPage from './components/PickQuestionsPage.vue'
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
import {router} from "@/router";

const count = ref(0)
const socket_server_url = "ws://188.68.222.147"

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
      is_connected: false, // подсоединен ли сокет

      players: [], // список игроков в нашей группе
      leading: false,
      round: 0,

      current_question: "____"

    }
  },

  mounted(){

    // создаем прокси для методов
    const self = this

    // Создаем сокет
    this.socket = io(socket_server_url);

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

      console.log("APP:SOCKET client/game_updated")

      // запоминаем код и игроков
      self.setCode(received_data.code)
      self.setPlayers(received_data.players)


      console.log(received_data)

      self.$forceUpdate();

      //  как только набралось два игрока – начинаем играть

      if (self.players.length == 2) {

        if (self.leading) {
          router.push('/pickquestion');
        } else {
          router.push('/waitforpick');
        }

        console.log("APP: 2 players detected, game starts")

      }

    });

    this.socket.on('client/receive_question', function (received_data){

      console.log("APP:SOCKET client/receive_question", received_data)

      self.current_question = received_data.text

      router.push("answerquestion")
      self.round ++

    })

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
