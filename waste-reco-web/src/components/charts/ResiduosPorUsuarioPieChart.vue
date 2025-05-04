<template>
  <div class="bg-white rounded-lg shadow-sm p-6">
    <h2 class="text-xl font-semibold text-gray-800 mb-4 border-b pb-3">Distribución de Residuos</h2>

    <!-- Contenedor de información y gráfico -->
    <div class="flex flex-col md:flex-row">
      <!-- Panel de información -->
      <div class="w-full md:w-1/3 mb-4 md:mb-0 md:pr-4">
        <div class="bg-gray-50 rounded-lg p-4">
          <div class="mb-4">
            <div class="text-sm text-gray-500">Cantidad total de residuos</div>
            <div class="text-2xl font-semibold text-teal-600">{{ totalResiduos }}</div>
          </div>

          <!-- Lista de tipos con colores -->
          <div v-if="chartData.labels.length > 0" class="space-y-2 mt-4">
            <div class="text-sm font-medium text-gray-600 mb-2">Tipos de residuos:</div>
            <div
              v-for="(label, index) in chartData.labels"
              :key="index"
              class="flex items-center text-sm"
            >
              <div
                class="w-3 h-3 rounded-full mr-2"
                :style="{ backgroundColor: chartData.datasets[0].backgroundColor[index] }"
              ></div>
              <span>{{ label }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Gráfico -->
      <div class="w-full md:w-2/3 flex items-center justify-center">
        <div class="w-full max-w-md h-auto">
          <Pie v-if="chartData.labels.length > 0" :data="chartData" :options="chartOptions" />
          <div v-else class="flex flex-col items-center justify-center h-full text-gray-500">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-12 w-12 mb-2 text-gray-400"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
              />
            </svg>
            <p>Cargando datos del reporte...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, watch } from 'vue'
import { storeToRefs } from 'pinia'
import { useReporteStore } from '@/stores/prediccionStore'
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement)

// ✅ usuarioId ahora es opcional
const props = defineProps<{ usuarioId?: number }>()

const reporteStore = useReporteStore()
const { reportes } = storeToRefs(reporteStore)

onMounted(async () => {
  if (props.usuarioId) {
    await reporteStore.getPrediccionByUsuario(props.usuarioId)
  } else {
    await reporteStore.getAllReportes()
  }
})

watch(
  () => props.usuarioId,
  async (newId) => {
    if (newId) {
      await reporteStore.getPrediccionByUsuario(newId)
    } else {
      await reporteStore.getAllReportes()
    }
  },
)

const colors = [
  '#14b8a6',
  '#0ea5e9',
  '#8b5cf6',
  '#ec4899',
  '#f59e0b',
  '#10b981',
  '#6366f1',
  '#ef4444',
  '#84cc16',
  '#3b82f6',
]

const chartData = computed(() => {
  const residuosCount: Record<string, number> = {}
  reportes.value.forEach((r) => {
    const nombre = r.residuo.tipo_residuo.nombre
    residuosCount[nombre] = (residuosCount[nombre] || 0) + 1
  })

  const labels = Object.keys(residuosCount)
  const data = Object.values(residuosCount)

  return {
    labels,
    datasets: [
      {
        label: 'Cantidad de residuos predichos',
        data,
        backgroundColor: labels.map((_, i) => colors[i % colors.length]),
      },
    ],
  }
})

const totalResiduos = computed(
  () => chartData.value.datasets[0].data.reduce((sum, val) => sum + val, 0) || 0,
)

const chartOptions = {
  responsive: true,
  maintainAspectRatio: true,
  plugins: {
    legend: { display: false },
    tooltip: {
      enabled: true,
      callbacks: {
        label: function (context: any) {
          const label = context.label || ''
          const value = context.raw || 0
          const percentage = ((value / totalResiduos.value) * 100).toFixed(1)
          return `${label}: ${value} (${percentage}%)`
        },
      },
    },
  },
}
</script>
