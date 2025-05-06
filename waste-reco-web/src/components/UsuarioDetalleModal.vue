<template>
  <div
    v-if="visible"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-60 transition-opacity duration-300"
  >
    <div
      class="bg-white rounded-xl shadow-xl max-w-5xl w-full overflow-hidden transform transition-all duration-300 ease-out"
      :class="{ 'scale-95 opacity-0': !visible, 'scale-100 opacity-100': visible }"
    >
      <!-- Header -->
      <div class="bg-teal-500 px-6 py-4 flex justify-between items-center">
        <h2 class="text-2xl font-semibold text-white">Reporte del Usuario</h2>
        <button
          @click="$emit('close')"
          class="text-white hover:bg-teal-600 rounded-full p-1 transition-colors duration-200"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Content -->
      <div class="p-6">
        <!-- Usuario Info Card -->
        <div class="bg-gray-50 rounded-lg p-5 shadow-sm mb-6" v-if="usuario">
          <div class="grid md:grid-cols-4 gap-4">
            <div class="flex items-center">
              <div class="bg-teal-100 p-3 rounded-full mr-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-teal-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
              </div>
              <div>
                <p class="text-sm text-gray-500">ID Usuario</p>
                <p class="font-medium">{{ usuario.id }}</p>
              </div>
            </div>
            <div class="flex items-center">
              <div class="bg-teal-100 p-3 rounded-full mr-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-teal-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                  />
                </svg>
              </div>
              <div>
                <p class="text-sm text-gray-500">Nombre</p>
                <p class="font-medium">{{ usuario.nombre }}</p>
              </div>
            </div>
            <div class="flex items-center">
              <div class="bg-teal-100 p-3 rounded-full mr-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-teal-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                  />
                </svg>
              </div>
              <div>
                <p class="text-sm text-gray-500">Email</p>
                <p class="font-medium">{{ usuario.email }}</p>
              </div>
            </div>
            <div class="flex items-center justify-end">
              <button
                class="group relative px-4 py-2 bg-teal-600 hover:bg-teal-700 text-white font-medium rounded-lg transition-all duration-200 ease-in-out flex items-center shadow-md hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-50"
                @click="enviarReporte(depositos)"
              >
                <span class="flex items-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 mr-2"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
                    />
                  </svg>
                  Enviar reporte semanal
                </span>
              </button>
            </div>
          </div>
        </div>

        <!-- No User Info Message -->
        <div v-else class="bg-gray-50 p-6 rounded-lg mb-6 text-center">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-12 w-12 text-gray-400 mx-auto mb-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <p class="text-gray-500 text-lg">No se encontró información del usuario.</p>
        </div>

        <!-- Chart Section -->
        <div v-if="usuario" class="bg-white rounded-lg">
          <div class="bg-white rounded-lg p-1">
            <ResiduosUsuarioBarChart :usuarioId="usuario.id" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { watch, ref } from 'vue'
import { startOfWeek, endOfWeek, format } from 'date-fns'
import { useReporteStore } from '@/stores/prediccionStore'
import type { Usuario } from '@/models/Usuario'
import { useEmailStore } from '@/stores/emailStore'
import type { EmailPayload, WastePayload } from '@/models/EmailPayload'
import type { ReporteResponse } from '@/models/Reporte'
import ResiduosUsuarioBarChart from '@/components/charts/ResiduosPorUsuarioPieChart.vue'

const reporteStore = useReporteStore()
const emailStore = useEmailStore()

const { usuario, visible } = defineProps<{
  visible: boolean
  usuario: Usuario
}>()

defineEmits(['close'])

const startDate = format(startOfWeek(new Date(), { weekStartsOn: 1 }), 'yyyy-MM-dd')
const endDate = format(endOfWeek(new Date(), { weekStartsOn: 1 }), 'yyyy-MM-dd')

console.log('startDate:', startDate)
console.log('endDate:', endDate)
// Estado reactivo para almacenar los depósitos
const depositos = ref<WastePayload[]>([
  { categoria: 'Aprovechables', cantidad: 0 },
  { categoria: 'No Aprovechables', cantidad: 0 },
  { categoria: 'Organicos', cantidad: 0 },
  { categoria: 'Peligrosos', cantidad: 0 },
])

// Función para contar los residuos por tipo
const contarResiduosPorTipo = (predicciones: ReporteResponse[]): void => {
  predicciones.forEach((prediccion) => {
    const tipo = prediccion.residuo.tipo_residuo.nombre
    // Aumentamos el contador correspondiente dependiendo del tipo de residuo
    if (tipo === 'Aprovechables') {
      depositos.value[0].cantidad += 1
    } else if (tipo === 'No Aprovechables') {
      depositos.value[1].cantidad += 1
    } else if (tipo === 'Organicos') {
      depositos.value[2].cantidad += 1
    } else if (tipo === 'Peligrosos') {
      depositos.value[3].cantidad += 1
    }
  })
}

watch(
  () => visible,
  async (newVal) => {
    if (newVal) {
      console.log('Usuario:', usuario)
      depositos.value = [
        // resetear los valores
        { categoria: 'Aprovechables', cantidad: 0 },
        { categoria: 'No Aprovechables', cantidad: 0 },
        { categoria: 'Organicos', cantidad: 0 },
        { categoria: 'Peligrosos', cantidad: 0 },
      ]

      await reporteStore.getPrediccionByUsuario(usuario.id, startDate, endDate)
      console.log('Predicciones cargadas:', reporteStore.reportes)

      contarResiduosPorTipo(reporteStore.reportes)
      console.log('Datos de depósitos:', depositos.value)
    }
  },
  { immediate: false },
)

const formatFecha = (fecha: string): string => {
  const meses = [
    'enero',
    'febrero',
    'marzo',
    'abril',
    'mayo',
    'junio',
    'julio',
    'agosto',
    'septiembre',
    'octubre',
    'noviembre',
    'diciembre',
  ]

  const [year, month, day] = fecha.split('-').map(Number)
  const nombreMes = meses[month - 1]

  return `${day} de ${nombreMes} de ${year}`
}

const enviarReporte = async (depositos: WastePayload[]) => {
  const body: EmailPayload = {
    subject: 'Informe de residuos semanales',
    body: 'Aquí está el resumen de depósitos para esta semana.',
    to: usuario.email,
    start_date: formatFecha(startDate),
    end_date: formatFecha(endDate),
    depositos: depositos.map((item) => ({
      categoria: `Depósitos ${item.categoria}`,
      cantidad: item.cantidad,
    })),
  }

  try {
    await emailStore.sendEmail(body)
    console.log('Email enviado con éxito')
  } catch (error) {
    console.error('Error al enviar el email:', error)
  }
}
</script>
