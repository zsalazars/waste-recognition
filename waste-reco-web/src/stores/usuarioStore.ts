import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

interface Usuario {
  id: number
  nombre: string
  email: string
}

export const useUsuarioStore = defineStore('userStore', () => {
  const usuarios = ref<Usuario[]>([])
  const isLoading = ref<boolean>(false)
  const error = ref<string | null>(null)

  const fetchUsuarios = async () => {
    isLoading.value = true
    error.value = null
    try {
      const response = await axios.get('http://127.0.0.1:8000/usuarios')
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
    fetchUsuarios,
  }
})
