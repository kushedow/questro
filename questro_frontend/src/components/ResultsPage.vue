<template lang="pug">
.results-page

  header.text-center.m-4.mb-1
    h4 5 раундов позади
  br
  .player-score.card.m-4.mb-5
    div.row.m-4.text-center
      .col
        h5 Игрок 1
        h2 25
      .col
        h5 Игрок 2
        h2 18

  .controls.text-center.mb-3
    div.mb-4
      button.btn.btn-dark.btn-lg Еще по 5 вопросов
    div
      router-link(to="/").btn.btn-link В главное меню

</template>

<script>
export default {
  name: "ResultsPage"
}
</script>

<style lang="sass">

.results-page
  .controls
    .btn-link
      color: #000

</style>