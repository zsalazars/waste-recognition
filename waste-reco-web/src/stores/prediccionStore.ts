import { defineStore } from 'pinia'
import { ref } from 'vue'
import http from '@/utils/axios'
import type Reporte from '@/models/Prediccion'
import type { ReporteResponse } from '@/models/Prediccion'

export const useReporteStore = defineStore('reporteStore', () => {
  const reportes = ref<ReporteResponse[]>([])
  const isLoading = ref<boolean>(false)
  const error = ref<string | null>(null)

  const getAllReportes = async () => {
    isLoading.value = true
    error.value = null
    try {
      const response = await http.get('/prediccion')
      reportes.value = response.data
    } catch {
      error.value = 'Error fetching reports'
    } finally {
      isLoading.value = false
    }
  }

  const getPrediccionByUsuario = async (id: number, startDate?: string, endDate?: string) => {
    isLoading.value = true
    error.value = null

    try {
      let url = `/prediccion/usuario/${id}`

      if (startDate && endDate) {
        url += `?start_date=${startDate}&end_date=${endDate}`
      }

      const response = await http.get(url)
      reportes.value = response.data
    } catch {
      error.value = 'Error fetching user prediction'
    } finally {
      isLoading.value = false
    }
  }

  const createReporte = async (reporte: Reporte) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await http.post('/reportes/generar-reporte', reporte)
      reportes.value.push(response.data)
    } catch {
      error.value = 'Error creating report'
    } finally {
      isLoading.value = false
    }
  }

  return {
    reportes,
    isLoading,
    error,
    getAllReportes,
    getPrediccionByUsuario,
    createReporte,
  }
})
