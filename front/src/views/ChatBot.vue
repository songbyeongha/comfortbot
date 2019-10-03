<template>
  <v-layout row wrap>
    <Background></Background>
    <ChatRoom></ChatRoom>
  </v-layout>
</template>

<script>
export default {
  name: "ChatBot",
  components: {
    ChatRoom: () => import("../components/ChatRoom.vue"),
    Background: () => import("../components/Background.vue")
  },
  data: () => ({
    //
  })
};
</script>
