import { createRouter, createWebHistory } from 'vue-router'
import AdminLayout from '@/layouts/AdminLayout.vue'
import AuthLayout from '@/layouts/AuthLayout.vue'
import LoginView from '@/views/LoginView.vue'
import UsuariosView from '@/views/UsuariosView.vue'
import ResiduosVuew from '@/views/ResiduosVuew.vue'
import ReportesView from '@/views/ReportesView.vue'
import DashboardView from '@/views/DashboardView.vue'

const routes = [
  {
    path: '/',
    component: AuthLayout,
    children: [{ path: '', name: 'login', component: LoginView }],
  },
  {
    path: '/admin',
    component: AdminLayout,
    children: [
      { path: '/dashboard', name: 'dashboard', component: DashboardView },
      { path: '/usuarios', name: 'usuarios', component: UsuariosView },
      { path: '/residuos', name: 'residuos', component: ResiduosVuew },
      { path: '/reportes', name: 'reportes', component: ReportesView },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// router.beforeEach((to, from, next) => {
//   const isAuthenticated = localStorage.getItem('token') // Simula autenticación

//   if (to.path.startsWith('/admin') && !isAuthenticated) {
//     next('/')
//   } else {
//     next()
//   }
// })

export default router
