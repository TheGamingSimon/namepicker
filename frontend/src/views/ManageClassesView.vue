<template>
  <h2>Klassen verwalten</h2>

  <AddClassForm @created="loadClasses" />

  <div v-for="cls in classes" :key="cls.id">
    <h3>{{ cls.name }}</h3>

    <StudentList :classId="cls.id" />
    <AddStudentForm :classId="cls.id" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import AddClassForm from '../components/AddClassForm.vue'
import StudentList from '../components/Studenlist.vue'
import AddStudentForm from '../components/AddStudentForm.vue'

const classes = ref([])

async function loadClasses() {
  const res = await api.get('/classes')
  classes.value = res.data
}

onMounted(loadClasses)
</script>
