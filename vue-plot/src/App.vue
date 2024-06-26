<script setup lang="ts">
import axios from "axios";
import { ref } from "vue";

const endpoint = import.meta.env.VITE_API_ENDPOINT as string;

const message = ref<string>("Push the button!");

const handleClick = () => {
  const config = {
    method: "post",
    url: endpoint + "/message",
  };
  
  // Python側に処理をリクエストする
  axios(config)
    .then((response) => {
      console.log(response);
      response.data.message && (message.value = response.data.message);
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<template>
  <div>
    <button type="button" @click="handleClick">{{ message }}</button>
  </div>
</template>
