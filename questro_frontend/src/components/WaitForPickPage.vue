<template lang="pug">
.answer-question
  header.text-center.m-4
    a(href="/").mr-3 Назад
    span &nbsp;&nbsp;&nbsp;&nbsp;
    span.ml-3 Раунд {{round}}

  h3.text-center.m-5 Давайте послушаем, какой вопрос выберет напарник

</template>

<script>
export default {

  data() {
    return {

    }
  },

  computed: {
    round() {return this.$root.$data.round}
  },

}
</script>

<style lang="sass">

</style>