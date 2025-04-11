import { defineStore } from 'pinia'
import { ref } from 'vue'
import http from '@/utils/axios'
import type Reporte from '@/models/Reporte'

export const useReporteStore = defineStore('reporteStore', () => {
  const reportes = ref<Reporte[]>([])
  const isLoading = ref<boolean>(false)
  const error = ref<string | null>(null)

  const getAllReportes = async () => {
    isLoading.value = true
    error.value = null
    try {
      const response = await http.get('/reportes')
      reportes.value = response.data
    } catch {
      error.value = 'Error fetching reports'
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
    createReporte,
  }
})
