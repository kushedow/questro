<script setup>

import QuestionsPage from './components/PickQuestionsPage.vue'
import MainMenuPage from './components/MainMenuPage.vue'
import {ref} from 'vue'

</script>

<template lang="pug">
.main-container
  .status.text-center
    span.badge.bg-success(v-if="is_connected") online
    span.badge.bg-danger(v-else) offline
  RouterView
  footer.text-center

.debug.text-center
  span leading:{{leading}} /&nbsp;
  span code:{{code}} /&nbsp;
  span players:{{players.length}} /&nbsp;
  span cat:{{current_category}}


</template>

<script>

import {io} from "socket.io-client";
import {router} from "@/router";

const count = ref(0)
// const socket_server_url = "ws://188.68.222.147"
const socket_server_url = "ws://0.0.0.0"

export default {

  methods: {

    // обновяем код
    setCode(new_code) {
      this.code = new_code
    },

    // обновляем игрока
    setPlayers(new_players) {
      this.players = new_players
    },

    // обновляем категории (обычно при подключении к игре)
    setCategories(categories) {
      this.categories = categories
    },


  },

  data() {
    return {

      socket: {},  // объект доступа к сокету
      code: "____",   // код присоединения к игре
      is_connected: false, // подсоединен ли сокет

      players: [], // список игроков в нашей группе
      leading: false,
      round: 0,

      categories: [],
      current_category: "default",

      current_question: "____"

    }
  },


  mounted() {

    // создаем прокси для методов
    const self = this

    // Создаем сокет
    this.socket = io(socket_server_url);

    // КОГДА ПРИСОЕДИНИЛИСЬ

    this.socket.on("connect", () => {

      this.is_connected = true

      router.push("/")

      console.log("APP: SOCKET connected")

    });

    // КОГДА ДИСКОННЕКТ

    this.socket.on("disconnect", () => {
      this.is_connected = false
      console.log("APP: SOCKET disconnected")
      alert("APP: DISCONNECTED")
    });

    // КОГДА ПРОИЗОШЛА ОШИБКА

    this.socket.on('client/exception', function (received_data) {

      alert(received_data.error)

    });

    // КОГДА ИГРА ОБНОВЛЕНА

    this.socket.on('client/game_updated', function (received_data) {

      console.log("APP: SOCKET client/game_updated")

      // запоминаем код и игроков
      self.setCode(received_data.code)
      self.setPlayers(received_data.players)

      //  как только набралось два игрока – начинаем играть
      //  но если есть код можно присоединиться еще игрокам

      if (self.players.length >= 2) {

        if (self.leading) {
          router.push('/pickquestion');
        } else {
          router.push('/waitforpick');
        }

        console.log("APP: 2 players detected, game starts")
      }

    });

    // КОГДА ВОПРОС ПОЛУЧЕН

    this.socket.on('client/receive_question', function (received_data) {

      console.log("APP: SOCKET client/receive_question", received_data)

      self.current_question = received_data.text

      router.push("answerquestion")
      self.round++

    })

    // КОГДА ПОЛУЧЕН СПИСОК КАТЕГОРИЙ

    this.socket.on('client/get_categories', function (received_data) {

      console.log("APP: SOCKET client/get_categories", received_data)

      // сохраняем полученные вопросы
      self.setCategories(received_data)

    })

  },

}

</script>

<style lang="sass">

body
  background-color: #222

.main-container
  background-color: #eee
  width: 420px
  padding: 16px
  margin: 2rem auto 2rem
  border: 1px solid #eee
  border-radius: 8px

  .status
    position: relative

    .badge
      position: absolute
      right: 0
      top: 0

.debug
  color: #888

</style>
