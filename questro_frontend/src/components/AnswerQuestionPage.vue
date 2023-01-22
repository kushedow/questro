<template lang="pug">

.answer-question
  header.text-center.m-4
    a(href="/").mr-3 Назад
    span &nbsp;&nbsp;&nbsp;&nbsp;
    span.ml-3 Раунд {{round}}

  h3.text-center.mt-5.mb-5 Вам прислали вопрос:

  .card.text-center.m-3.mt-4.mb-5.p-5
    h2 {{ current_question }}

  .text-center.mb-4
    button.btn-lg.btn.btn-primary.btn-dark(@click="confirmAnswer()") Готово, дальше!

</template>

<script>

import {router} from "@/router";

export default {

  methods: {

    confirmAnswer(){

      router.push("pickquestion")

    }

  },

  computed: {

    round() { return this.$root.$data.round },
    current_question() {return this.$root.$data.current_question }

  },

  data() {
    return {

    }
  },

}

</script>

<style lang="sass">

header
  a
    color: #444

</style>