<template lang="pug">
.main-menu-page

    header.text-center.m-3.mb-5
        h2.text-center.mt-3.mb-4 Questro
        h4.text-center Помогаем оживить общение, сломать лед, узнать друг друга лучше и найти общие темы

    .list-group.text-center

         router-link(to="/create").list-group-item.list-group-item-action Создать
         router-link(to="/join").list-group-item.list-group-item-action Присоединиться
         router-link(to="/categories").list-group-item.list-group-item-action Наборы вопросов
         // router-link(to="results").list-group-item.list-group-item-action Результаты

    footer.m-3.mt-5.text-center
        a(href="http://www.t.me/kushedow", target="_blank") Подружиться с автором

</template>

<script>

export default {

  data() {
    return {
        foo: {},
    }
  },

  methods: {

  }
}

</script>

<style lang="sass">

.main-menu-page

  footer
    a
      color: #444

  .list-group-item
    padding-top: 2rem
    padding-bottom: 2rem


</style>
