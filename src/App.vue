<script setup>
import { onMounted } from 'vue';
onMounted(async () => {
  const response = await fetch('/api/users');
  const data = await response.json();
  console.log(data);
});
</script>

<template>
  <el-date-picker type="date" placeholder="date"></el-date-picker>
</template>

<style>
#app {
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
}
</style>
