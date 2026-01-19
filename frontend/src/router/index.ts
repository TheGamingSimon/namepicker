import { createRouter, createWebHistory } from 'vue-router'
import PickNamesView from '@/views/PickNamesView.vue'
import ManageClassesView from '@/views/ManageClassesView.vue'

const routes = [
  { path: '/', component: PickNamesView },
  { path: '/classes', component: ManageClassesView }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
