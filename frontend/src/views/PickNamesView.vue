<template>
  <h2>Namen ziehen</h2>

  <ClassSelector v-model="selectedClassId" />

  <input
    type="number"
    v-model="count"
    min="1"
    placeholder="Anzahl Namen"
  />

  <button @click="pickNames">Picken</button>

  <ul>
    <li v-for="name in pickedNames" :key="name">{{ name }}</li>
  </ul>
</template>

<script setup>
import { ref } from 'vue'
import ClassSelector from '../components/ClassSelector.vue'
import api from '../services/api'

const selectedClassId = ref(null)
const count = ref(1)
const pickedNames = ref([])

async function pickNames() {
  const res = await api.post(
    `/classes/${selectedClassId.value}/pick`,
    null,
    { params: { count: count.value } }
  )
  pickedNames.value = res.data
}
</script>
