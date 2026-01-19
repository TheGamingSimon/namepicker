<template>
  <select
    :value="modelValue"
    @change="onChange"
  >
    <option disabled value="">Klasse auswählen</option>
    <option v-for="c in classes" :key="c.id" :value="c.id">
      {{ c.name }}
    </option>
  </select>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'

const props = defineProps({
  modelValue: [String, Number]
})

const emit = defineEmits(['update:modelValue'])

const classes = ref([])

function onChange(event) {
  emit('update:modelValue', event.target.value)
}

onMounted(async () => {
  const res = await api.get('/classes')
  classes.value = res.data
})
</script>
    