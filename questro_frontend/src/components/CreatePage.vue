<template lang="pug">

.create-page
  header.text-center.mt-3.mb-5
    router-link(to="/").btn.btn-link Назад

  h4.text-center Передайте этот код вашему напарнику

  p.giant.text-center.m-0 {{ code }}

  p.status.text-center Пользователей: {{ players.length}}

  .actions.text-center.mt-5.mb-4

    router-link(to="/pickquestion", v-if="players.length==2").btn.btn-dark.btn-lg Начать

</template>

<script>
export default {

  name: "CreatePage",

  methods: {

  },

  data() {
    return {
      socket:  this.$root.$data.socket,
    }
  },

  computed: {
    // код присоединения к игре
    code() {return this.$root.$data.code},
    // игроки в текущей игровой сессии
    players() {return this.$root.$data.players},
    // выбранная категория
    current_category() {return this.$root.$data.current_category},
  },

  mounted() {
    console.log("APP: отправляем запрос над создание игры")

    // заказываем категории
    this.socket.emit("server/get_categories", {})

    // отправляем запрос на создание игры
    this.socket.emit("server/create_game", {cat: this.current_category})

    // обозначаем, что в игре мы отвечаем первыми
    this.$root.$data.leading = true

    // сбрасываем счетчик раундов на 0
    this.$root.$data.round = 0

  },

}
</script>

<style lang="sass">

.create-page

  .btn-link
    color: #444

  .giant
    font-size: 6rem

</style>
