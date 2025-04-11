import { defineStore } from 'pinia'
import { ref } from 'vue'
import http from '@/utils/axios'
import type { ResiduoCategoria } from '@/models/Residuo'

export const useResiduoStore = defineStore('residuoStore', () => {
  const residuosByCategorias = ref<ResiduoCategoria[]>([])
  const isLoading = ref<boolean>(false)
  const error = ref<string | null>(null)

  const getAllResiduos = async () => {
    isLoading.value = true
    error.value = null
    try {
      const response = await http.get('/residuos/categorias')
      residuosByCategorias.value = response.data
    } catch {
      error.value = 'Error fetching reports'
    } finally {
      isLoading.value = false
    }
  }

  return {
    residuosByCategorias,
    isLoading,
    error,
    getAllResiduos,
  }
})
