<template>
  <div class="bg-gray-50 min-h-screen">
    <!-- Sección superior con filtros y fechas -->
    <div class="bg-white shadow-sm rounded-lg p-6 mb-6">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6">
        <div>
          <h1 class="text-2xl font-bold text-gray-800">Panel de Reportes</h1>
          <p class="text-gray-500 mt-1">Estadísticas y análisis de datos de residuos</p>
        </div>
        <div class="mt-4 md:mt-0 flex space-x-2">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                />
              </svg>
            </div>
            <input
              type="date"
              class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-green-500 focus:border-green-500"
            />
          </div>

          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                />
              </svg>
            </div>
            <input
              type="date"
              class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-green-500 focus:border-green-500"
            />
          </div>

          <button
            class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg flex items-center shadow-sm transition-colors duration-200"
          >
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
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
              />
            </svg>
            Exportar
          </button>
        </div>
      </div>

      <div class="flex flex-wrap -mx-2">
        <div class="px-2 w-full sm:w-1/2 md:w-1/4 mb-4">
          <select
            class="block w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-green-500 focus:border-green-500"
          >
            <option value="">Todos los residuos</option>
            <option value="organico">Orgánico</option>
            <option value="plastico">Plástico</option>
            <option value="papel">Papel</option>
            <option value="vidrio">Vidrio</option>
            <option value="metal">Metal</option>
          </select>
        </div>

        <div class="px-2 w-full sm:w-1/2 md:w-1/4 mb-4">
          <select
            class="block w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-green-500 focus:border-green-500"
          >
            <option value="">Todos los centros</option>
            <option value="centro1">Centro de Reciclaje Norte</option>
            <option value="centro2">Centro de Reciclaje Sur</option>
            <option value="centro3">Centro de Reciclaje Este</option>
          </select>
        </div>

        <div class="px-2 w-full sm:w-1/2 md:w-1/4 mb-4">
          <select
            class="block w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-green-500 focus:border-green-500"
          >
            <option value="dia">Diario</option>
            <option value="semana">Semanal</option>
            <option value="mes">Mensual</option>
            <option value="ano">Anual</option>
          </select>
        </div>

        <div class="px-2 w-full sm:w-1/2 md:w-1/4 mb-4">
          <button
            class="w-full bg-teal-600 hover:bg-teal-700 text-white px-4 py-2 rounded-lg flex items-center justify-center shadow-sm transition-colors duration-200"
          >
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
                d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
              />
            </svg>
            Aplicar Filtros
          </button>
        </div>
      </div>
    </div>

    <!-- Tarjetas de Estadísticas KPI -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
      <div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-green-500">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-gray-500">Total de Residuos</p>
            <h3 class="text-2xl font-bold text-gray-800 mt-1">8,742 kg</h3>
            <p class="text-xs text-green-600 mt-1 flex items-center">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-3 w-3 mr-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                />
              </svg>
              +12.5% vs. mes anterior
            </p>
          </div>
          <div class="bg-green-100 p-3 rounded-full">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6 text-green-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"
              />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-blue-500">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-gray-500">Tasa de Reciclaje</p>
            <h3 class="text-2xl font-bold text-gray-800 mt-1">68.7%</h3>
            <p class="text-xs text-green-600 mt-1 flex items-center">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-3 w-3 mr-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                />
              </svg>
              +3.2% vs. mes anterior
            </p>
          </div>
          <div class="bg-blue-100 p-3 rounded-full">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6 text-blue-600"
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
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-yellow-500">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-gray-500">Precisión de Reconocimiento</p>
            <h3 class="text-2xl font-bold text-gray-800 mt-1">94.3%</h3>
            <p class="text-xs text-green-600 mt-1 flex items-center">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-3 w-3 mr-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                />
              </svg>
              +1.8% vs. mes anterior
            </p>
          </div>
          <div class="bg-yellow-100 p-3 rounded-full">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6 text-yellow-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
              />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-purple-500">
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-gray-500">Huella Carbono Reducida</p>
            <h3 class="text-2xl font-bold text-gray-800 mt-1">3.8 tons</h3>
            <p class="text-xs text-green-600 mt-1 flex items-center">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-3 w-3 mr-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                />
              </svg>
              +7.9% vs. mes anterior
            </p>
          </div>
          <div class="bg-purple-100 p-3 rounded-full">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6 text-purple-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Gráficos y Visualizaciones -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
      <!-- Gráfico de clasificacion de residuos -->
      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-semibold text-gray-800">Reconocimiento de Residuos</h3>
          <div class="flex space-x-2">
            <button class="px-3 py-1 text-xs bg-green-50 text-green-700 rounded-full">
              Diario
            </button>
            <button class="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full">
              Semanal
            </button>
            <button class="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full">
              Mensual
            </button>
          </div>
        </div>

        <div class="h-80 flex items-center justify-center">
          <!-- Aquí iría la gráfica de precisión de reconocimiento de residuos -->
          <div class="w-full h-full bg-gray-50 rounded-lg flex items-center justify-center">
            <ResiduosBarChart />
          </div>
        </div>
      </div>

      <!-- Gráfico de clasificacion de usuarios -->
      <div class="bg-white rounded-lg shadow-sm p-6">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-semibold text-gray-800">Reconocimiento de usuarios</h3>
          <div class="flex space-x-2">
            <button class="px-3 py-1 text-xs bg-green-50 text-green-700 rounded-full">
              Diario
            </button>
            <button class="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full">
              Semanal
            </button>
            <button class="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full">
              Mensual
            </button>
          </div>
        </div>

        <div class="h-80 flex items-center justify-center">
          <!-- Aquí iría la gráfica de precisión de reconocimiento facial -->
          <div class="w-full h-full bg-gray-50 rounded-lg flex items-center justify-center">
            <UsuariosBarChart />
          </div>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
      <!-- Mapa de calor por ubicación -->
      <div class="bg-white rounded-lg shadow-sm p-6 lg:col-span-2">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-semibold text-gray-800">Distribución Geográfica</h3>
          <select
            class="block border border-gray-300 rounded-lg px-3 py-1 text-sm focus:ring-green-500 focus:border-green-500"
          >
            <option value="all">Todos los residuos</option>
            <option value="organico">Orgánico</option>
            <option value="plastico">Plástico</option>
            <option value="papel">Papel</option>
          </select>
        </div>

        <div class="h-80 flex items-center justify-center">
          <!-- Aquí iría un mapa de calor geográfico -->
          <div class="w-full h-full bg-gray-50 rounded-lg flex items-center justify-center">
            <p class="text-gray-500">Mapa de distribución geográfica de residuos</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import ResiduosBarChart from '@/components/ResiduosBarChart.vue'
import UsuariosBarChart from '@/components/UsuariosBarChart.vue'
</script>
