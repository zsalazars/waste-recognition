import { defineStore } from 'pinia'
import { ref } from 'vue'
import http from '@/utils/axios'
import type { Usuario } from '@/models/Usuario'

export const useUsuarioStore = defineStore('userStore', () => {
  const usuarios = ref<Usuario[]>([])
  const isLoading = ref<boolean>(false)
  const error = ref<string | null>(null)

  const getAllUsuarios = async () => {
    isLoading.value = true
    error.value = null
    try {
      const response = await http.get('/usuarios')
      usuarios.value = response.data
    } catch {
      error.value = 'Error fetching users'
    } finally {
      isLoading.value = false
    }
  }

  return {
    usuarios,
    isLoading,
    error,
    getAllUsuarios,
  }
})
