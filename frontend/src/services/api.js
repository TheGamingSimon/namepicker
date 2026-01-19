import axios from 'axios'

export default axios.create({
  baseURL: '/api'
})

// Klasse
export const getClasses = () => api.get('/classes')
export const getClass = (id) => api.get(`/classes/${id}`)
export const createClass = (name) =>
  api.post('/classes', { name })
export const updateClass = (id, name) =>
  api.put(`/classes/${id}`, { name })
export const deleteClass = (id) =>
  api.delete(`/classes/${id}`)

// Schüler
export const getStudents = () => api.get('/students')
export const getStudent = (id) => api.get(`/students/${id}`)
export const createStudent = (name, class_id) =>
  api.post('/students', { name, class_id })
export const updateStudent = (id, name, class_id) =>
  api.put(`/students/${id}`, { name, class_id })
export const deleteStudent = (id) =>
  api.delete(`/students/${id}`)

// Name picken
export const pickNames = (class_id, count) =>
  api.post(`/classes/${class_id}/pick?count=${count}`)

export default api
