<template>
  <ul>
    <li v-for="s in students" :key="s.id">
      {{ s.name }}
      <button @click="remove(s.id)">❌</button>
    </li>
  </ul>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const props = defineProps(['classId'])
const students = ref([])

async function load() {
  const res = await api.get('/students', {
    params: { classId: props.classId }
  })
  students.value = res.data
}

async function remove(id) {
  await api.delete(`/students/${id}`)
  load()
}

onMounted(load)
</script>