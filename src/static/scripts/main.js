//const { createApp } = Vue
//
//
//
//////////////////////////////
////      CREATE APP       ///
//////////////////////////////
//
//app = Vue.createApp({
//
//    setup() {
//        const store = 'init'
//    },
//
//    data() {
//      return {
//        message: 'Hello Vue!',
//        //boo: this.store.page,
//      }
//    }
//
//}).mount('#app')
//
//
//
///////////////////////
/////  S O C K E T  ///
///////////////////////
//
//const socket = io("ws://0.0.0.0:5001/");
//
//socket.on("connect", () => {
//  console.log("connected")
//  console.log(socket.id);
//});
//
//socket.on("client/welcome", ({ type, data }) => {
//    console.log("client/welcome")
//});
//
//socket.on("disconnect", () => {
//  console.log("connected")
//  console.log(socket.id); // undefined
//});
//
//console.log("Оно работает")
//
//
