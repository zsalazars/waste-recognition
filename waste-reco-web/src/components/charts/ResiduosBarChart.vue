<template>
  <div class="p-6 space-y-5">
    <h2 class="text-2xl text-center font-bold pt-5">Rendimiento del modelo por residuo</h2>

    <Bar v-if="chartData.labels.length > 0" :data="chartData" :options="chartOptions" />

    <div v-else class="text-gray-500">Cargando datos del reporte...</div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useReporteStore } from '@/stores/prediccionStore'

import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

// Registrar los componentes necesarios
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const reporteStore = useReporteStore()
const { reportes } = storeToRefs(reporteStore)

onMounted(async () => {
  await reporteStore.getAllReportes()
})

const chartData = computed(() => {
  // Clasificar ahora por residuo
  const residuos: Record<number, { nombre: string; sum: number; count: number }> = {}

  reportes.value.forEach((r) => {
    const id = r.residuo.id
    const nombre = r.residuo.nombre

    if (!residuos[id]) {
      residuos[id] = { nombre, sum: 0, count: 0 }
    }

    residuos[id].sum += parseFloat(r.tasa_acierto.toString())
    residuos[id].count += 1
  })

  const labels = Object.values(residuos).map((residuo) => residuo.nombre)
  const data = Object.values(residuos).map((residuo) => (residuo.sum / residuo.count) * 100)

  return {
    labels,
    datasets: [
      {
        label: 'Precisión promedio por residuo (%)',
        backgroundColor: '#38bdf8',
        data,
      },
    ],
  }
})

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top' as const,
    },
    tooltip: {
      enabled: true,
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      max: 100,
    },
  },
}
</script>
