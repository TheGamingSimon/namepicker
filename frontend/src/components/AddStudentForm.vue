F<template>
  <input v-model="name" placeholder="Schülername" />
  <button @click="add">Hinzufügen</button>
</template>

<script setup>
import { ref } from 'vue'
import api from '../services/api'

const props = defineProps(['classId'])
const name = ref('')

async function add() {
  await api.post('/students', {
    name: name.value,
    classId: props.classId
  })
  name.value = ''
}
</script>
