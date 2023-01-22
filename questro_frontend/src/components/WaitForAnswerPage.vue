<template lang="pug">
.answer-question
  header.text-center.m-4
    a(href="/").mr-3 Назад
    span &nbsp;&nbsp;&nbsp;&nbsp;
    span.ml-3 Раунд {{round}}
  .card.mt-5
    h3.text-center.m-5 {{ current_question }}
  h5.text-center.m-5 Давайте посмотрим, что ответит напарник!

</template>

<script>
export default {

  name: "WaitForAnswer.vue",

  computed: {
    round() {return this.$root.$data.round},
    current_question() {return this.$root.$data.current_question},
  },

}
</script>

<style lang="sass">

.answer-question
  min-height: 400px

</style>