<template>
  <v-app justify-center align-center>
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <router-view></router-view>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  components: {
  },
  data: () => ({
    //
  })
};
</script>
