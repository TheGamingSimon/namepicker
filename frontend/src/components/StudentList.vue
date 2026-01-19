<template>
  <div>
    <ul v-if="students.length">
      <li v-for="s in students" :key="s.id">
        {{ s.name }}
        <button @click="remove(s.id)">❌</button>
      </li>
    </ul>

    <!-- Nur Add-Form rendern, wenn es existiert -->
    <div v-if="!loading" class="add-student">
      <input
        v-model="newStudentName"
        placeholder="Schülername eingeben"
        @keyup.enter="addStudent"
      />
      <button @click="addStudent">Hinzufügen</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import api from '@/services/api'

const props = defineProps({
  classId: {
    type: [String, Number],
    required: true
  }
})

const students = ref([])
const newStudentName = ref('')
const loading = ref(true)

async function loadStudents() {
  if (!props.classId) return
  loading.value = true
  try {
    const res = await api.get('/students', { params: { classId: props.classId } })
    students.value = res.data
  } catch (err) {
    console.error(err)
    students.value = []
  } finally {
    loading.value = false
  }
}

async function addStudent() {
  if (!newStudentName.value.trim()) return
  try {
    await api.post('/students', {
      name: newStudentName.value,
      classId: props.classId
    })
    newStudentName.value = ''
    loadStudents()
  } catch (err) {
    console.error(err)
  }
}

async function remove(id) {
  try {
    await api.delete(`/students/${id}`)
    loadStudents()
  } catch (err) {
    console.error(err)
  }
}

onMounted(loadStudents)
watch(() => props.classId, loadStudents)
</script>
