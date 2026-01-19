<template>
  <input v-model="name" placeholder="Neue Klasse" />
  <button @click="create">Erstellen</button>
</template>

<script setup>
import { ref } from 'vue'
import api from '../services/api'

const emit = defineEmits(['created'])
const name = ref('')

async function create() {
  await api.post('/classes', { name: name.value })
  name.value = ''
  emit('created')
}
</script>
  