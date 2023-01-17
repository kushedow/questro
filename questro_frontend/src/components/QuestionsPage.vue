<template lang="pug">
.questions-page
    // верхняя статистика
    .counters.clearfix
      span.float-start Раунд {{round}}
      span.float-end Счет {{score}}

    div
      // заголовок
      h3.text-center.mt-4.mb-5 Выбери вопрос

      // карточка
      .card.sd-grid.gap-3.text-center.mb-5
          ul.list-group.list-group-flush
            li.list-group-item(v-for='que in questions')
              a.d-block.p-3(href="#")
                span.d-block.text.mb-2 {{ que }}
                span.badge.rounded-pill.bg-secondary 1 балл

    // нижние контролы
    .controls.text-center.mb-4
        button.btn.btn-light Заменить вопросы (-5 баллов)

</template>

<script>

export default {
  data() {
    return {
      round: 1,
      score: 0,
      questions: [
        "Какое любимое место",
        "У тебя есть один день, как ты его потратишь",
        "Был ли случай когда ты читал чужую переписку",
      ]
    }
  }
}

</script>

<style>

.questions-page .card a {
    color: #444;
    text-decoration: none;
}


</style>
