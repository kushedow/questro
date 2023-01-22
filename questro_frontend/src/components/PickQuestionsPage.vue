<template lang="pug">
.questions-page
  // верхняя статистика
  .create-page
    header.text-center.mt-3.mb-2
      router-link(to="/").btn.btn-link Назад

    div
      // заголовок
      h3.text-center.mt-3.mb-4 Выбери вопрос, чтобы отправить его

      // карточка
      .div(v-for='que in questions').text-center
        .card.sd-grid.gap-3.mb-3.p-4(@click="pickQuestion(que)")
          span.d-block.text {{que.text}}

    // нижние контролы
    .controls.text-center.mb-4.mt-5
        button.btn.btn-dark(@click="fetchQuestions") Следующие вопросы

</template>


<script>

import {router} from "@/router";

export default {

  data() {
    return {

      round: 1,
      socket: this.$root.$data.socket,
      is_loaded: false,
      questions: [],

    }
  },

  computed: {

  },

  methods: {

    // Получаем вопрос от сервера
    fetchQuestions() {
      this.socket.emit("server/get_questions", {count: 3})
    },

    pickQuestion(question){

      this.socket.emit("server/pick_question", {pk: question.pk})

      this.$root.$data.current_question = question.text

      router.push("/waitforanswer")

    }

  },

  mounted(){

    self = this
    this.fetchQuestions()

    // Обрабатываем ответ с вопросами
    this.socket.on('client/get_questions', function (received_data) {
      console.log("APP:client/get_questions", received_data)
      self.questions = received_data
    })

  }
}


</script>

<style>

.questions-page .card a {
    color: #444;
    text-decoration: none;
}

</style>
