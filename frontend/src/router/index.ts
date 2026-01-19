import { createRouter, createWebHistory } from 'vue-router'
import PickNamesView from '@/views/PickNamesView.vue'
import ManageClassesView from '@/views/ManageClassesView.vue'

const routes = [
  { path: '/', name: 'Home', component: PickNamesView },
  { path: '/classes', name: 'Classes', component: ManageClassesView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
