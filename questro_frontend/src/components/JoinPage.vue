// Страничка присоединения к игре

<template lang="pug">

.join-page
  header.text-center.mt-3.mb-2
    router-link(to="/").btn.btn-link Назад

  h4.text-center.p-4 Получите код от напарника по игре и введите его тут, чтобы присоединиться

  form.join-form.m-4.text-center
    input.giant(v-model='code', placeholder='0000').mb-5
    button(@click='joinGame').btn.btn-lg.btn-dark Мы готовы начать

</template>

<script setup>

</script>

<script>
export default {

  data() {
    return {
      socket:  this.$root.$data.socket,
      code: "",
    }
  },

  methods: {

    joinGame(){
      //console.log(this.socket.emit)

      this.socket.emit("server/join_game", {code: parseInt(this.code)})
      console.log("APP: отправляем запрос на присоедниение к игре", this.code)
    }

  },

  mounted() {



  },

}

</script>



<style lang="sass">

.join-page

  .btn-link
    color: #444444

  input.giant
    display: block
    width: 100%
    text-align: center
    font-size: 64px
    background-color: #fff

    border: none
    border-bottom: 3px solid #eee
    border-radius: 0.5rem

</style>