<template lang="pug">
.pick-category
  header.text-center.m-4
    a(href="/").mr-3 Назад

  .div(v-for='cat in categories').text-center
    .card.sd-grid.gap-3.mb-3.p-4(@click="setCategory(cat)")
      span.d-block.text {{cat.title}}

</template>

<script>
import {router} from "@/router";

export default {
  name: "PickCategoryPage",

  data() {
    return {
      socket: this.$root.$data.socket
    }
  },

  computed: {
    categories() {return this.$root.$data.categories}
  },

  methods: {

    setCategory(cat) {
      this.$root.$data.current_category = cat.code
      router.push("/create")
    },

  },


  mounted() {
    console.log("APP: отправляем запрос над создание игры")

    // заказываем категории
    this.socket.emit("server/get_categories", {})
  }

}
</script>

<style scoped lang="sass">

</style>