<template>
  <!-- Header con saludo y acciones rápidas -->
  <div class="bg-white shadow-sm rounded-lg p-6 mb-6">
    <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-gray-800">Bienvenido al Dashboard</h1>
        <p class="text-gray-500 mt-1">Resumen general del sistema de gestión de residuos</p>
      </div>
      <div class="mt-4 md:mt-0 flex space-x-2">
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
              d="M12 6v6m0 0v6m0-6h6m-6 0H6"
            />
          </svg>
          Nueva Recolección
        </button>
        <button
          class="bg-teal-600 hover:bg-teal-700 text-white px-4 py-2 rounded-lg flex items-center shadow-sm transition-colors duration-200"
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
          Ver Reportes
        </button>
      </div>
    </div>

    <!-- Resumen rápido de estadísticas -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div class="bg-green-50 rounded-lg p-4 text-center">
        <p class="text-sm text-green-700 font-medium">Recolecciones Hoy</p>
        <p class="text-2xl font-bold text-green-800 mt-1">24</p>
      </div>
      <div class="bg-blue-50 rounded-lg p-4 text-center">
        <p class="text-sm text-blue-700 font-medium">Residuos Pendientes</p>
        <p class="text-2xl font-bold text-blue-800 mt-1">8</p>
      </div>
      <div class="bg-purple-50 rounded-lg p-4 text-center">
        <p class="text-sm text-purple-700 font-medium">Centros Activos</p>
        <p class="text-2xl font-bold text-purple-800 mt-1">5</p>
      </div>
      <div class="bg-yellow-50 rounded-lg p-4 text-center">
        <p class="text-sm text-yellow-700 font-medium">Alertas</p>
        <p class="text-2xl font-bold text-yellow-800 mt-1">3</p>
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

  <!-- Gráficos principales y actividades recientes -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
    <!-- Gráfico principal -->
    <div class="bg-white rounded-lg shadow-sm p-6 lg:col-span-2">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-lg font-semibold text-gray-800">Resumen de Actividad</h3>
        <div class="flex space-x-2">
          <button class="px-3 py-1 text-xs bg-green-50 text-green-700 rounded-full">Semanal</button>
          <button class="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full">Mensual</button>
          <button class="px-3 py-1 text-xs bg-gray-100 text-gray-700 rounded-full">Anual</button>
        </div>
      </div>

      <div class="h-80 flex items-center justify-center">
        <!-- Aquí iría la gráfica de barras o líneas principal -->
        <div class="w-full h-full bg-gray-50 rounded-lg flex items-center justify-center">
          <p class="text-gray-500">Gráfico de actividad semanal</p>
        </div>
      </div>
    </div>

    <!-- Actividades recientes -->
    <div class="bg-white rounded-lg shadow-sm p-6">
      <h3 class="text-lg font-semibold text-gray-800 mb-4">Actividades Recientes</h3>

      <div class="space-y-4">
        <div class="flex items-start">
          <div class="bg-green-100 p-2 rounded-full mr-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-green-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
          </div>
          <div>
            <p class="text-sm font-medium">Recolección completada</p>
            <p class="text-xs text-gray-500">Centro Norte - 145kg</p>
            <p class="text-xs text-gray-400 mt-1">Hace 35 minutos</p>
          </div>
        </div>

        <div class="flex items-start">
          <div class="bg-blue-100 p-2 rounded-full mr-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-blue-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
              />
            </svg>
          </div>
          <div>
            <p class="text-sm font-medium">Nuevo reporte generado</p>
            <p class="text-xs text-gray-500">Reporte mensual - Marzo</p>
            <p class="text-xs text-gray-400 mt-1">Hace 2 horas</p>
          </div>
        </div>

        <div class="flex items-start">
          <div class="bg-yellow-100 p-2 rounded-full mr-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-yellow-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
              />
            </svg>
          </div>
          <div>
            <p class="text-sm font-medium">Alerta de capacidad</p>
            <p class="text-xs text-gray-500">Centro Sur - 85% capacidad</p>
            <p class="text-xs text-gray-400 mt-1">Hace 5 horas</p>
          </div>
        </div>

        <div class="flex items-start">
          <div class="bg-purple-100 p-2 rounded-full mr-3">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 text-purple-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
              />
            </svg>
          </div>
          <div>
            <p class="text-sm font-medium">Nuevo usuario</p>
            <p class="text-xs text-gray-500">María González - Operador</p>
            <p class="text-xs text-gray-400 mt-1">Hace 1 día</p>
          </div>
        </div>
      </div>

      <button
        class="w-full mt-4 text-sm text-green-600 font-medium hover:text-green-800 transition-colors duration-200"
      >
        Ver todas las actividades
      </button>
    </div>
  </div>

  <!-- Sección de atajos y resumen por categorías -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
    <!-- Distribución de residuos -->
    <div class="bg-white rounded-lg shadow-sm p-6">
      <h3 class="text-lg font-semibold text-gray-800 mb-4">Distribución por Tipo</h3>

      <div class="h-64 flex items-center justify-center mb-4">
        <!-- Aquí iría un gráfico de dona o pastel -->
        <div class="w-full h-full bg-gray-50 rounded-lg flex items-center justify-center">
          <p class="text-gray-500">Gráfico de distribución por tipo de residuo</p>
        </div>
      </div>

      <div class="space-y-2">
        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
            <span class="text-sm text-gray-600">Orgánico</span>
          </div>
          <span class="text-sm font-medium">42%</span>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-blue-500 rounded-full mr-2"></div>
            <span class="text-sm text-gray-600">Plástico</span>
          </div>
          <span class="text-sm font-medium">28%</span>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-yellow-500 rounded-full mr-2"></div>
            <span class="text-sm text-gray-600">Papel</span>
          </div>
          <span class="text-sm font-medium">18%</span>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-purple-500 rounded-full mr-2"></div>
            <span class="text-sm text-gray-600">Vidrio</span>
          </div>
          <span class="text-sm font-medium">12%</span>
        </div>
      </div>
    </div>

    <!-- Accesos rápidos -->
    <div class="bg-white rounded-lg shadow-sm p-6">
      <h3 class="text-lg font-semibold text-gray-800 mb-4">Accesos Rápidos</h3>

      <div class="grid grid-cols-2 gap-4">
        <div
          class="bg-green-50 rounded-lg p-4 flex flex-col items-center justify-center hover:bg-green-100 transition-colors duration-200 cursor-pointer"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-8 w-8 text-green-600 mb-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            />
          </svg>
          <span class="text-sm font-medium text-green-700">Nuevo Reporte</span>
        </div>

        <div
          class="bg-blue-50 rounded-lg p-4 flex flex-col items-center justify-center hover:bg-blue-100 transition-colors duration-200 cursor-pointer"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-8 w-8 text-blue-600 mb-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
            />
          </svg>
          <span class="text-sm font-medium text-blue-700">Estadísticas</span>
        </div>

        <div
          class="bg-yellow-50 rounded-lg p-4 flex flex-col items-center justify-center hover:bg-yellow-100 transition-colors duration-200 cursor-pointer"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-8 w-8 text-yellow-600 mb-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
            />
          </svg>
          <span class="text-sm font-medium text-yellow-700">Usuarios</span>
        </div>

        <div
          class="bg-purple-50 rounded-lg p-4 flex flex-col items-center justify-center hover:bg-purple-100 transition-colors duration-200 cursor-pointer"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-8 w-8 text-purple-600 mb-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
            />
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
            />
          </svg>
          <span class="text-sm font-medium text-purple-700">Configuración</span>
        </div>
      </div>
    </div>

    <!-- Próximas recolecciones -->
    <div class="bg-white rounded-lg shadow-sm p-6">
      <h3 class="text-lg font-semibold text-gray-800 mb-4">Próximas Recolecciones</h3>

      <div class="space-y-4">
        <div class="border-l-4 border-green-500 pl-3 py-1">
          <p class="text-sm font-medium">Centro Norte</p>
          <p class="text-xs text-gray-500">Mañana, 09:00 AM</p>
          <p class="text-xs bg-green-100 text-green-800 rounded-full px-2 py-0.5 inline-block mt-1">
            Programada
          </p>
        </div>

        <div class="border-l-4 border-blue-500 pl-3 py-1">
          <p class="text-sm font-medium">Centro Sur</p>
          <p class="text-xs text-gray-500">Mañana, 11:30 AM</p>
          <p class="text-xs bg-blue-100 text-blue-800 rounded-full px-2 py-0.5 inline-block mt-1">
            En preparación
          </p>
        </div>

        <div class="border-l-4 border-purple-500 pl-3 py-1">
          <p class="text-sm font-medium">Centro Este</p>
          <p class="text-xs text-gray-500">Miércoles, 10:15 AM</p>
          <p
            class="text-xs bg-purple-100 text-purple-800 rounded-full px-2 py-0.5 inline-block mt-1"
          >
            Pendiente
          </p>
        </div>
      </div>
      <button
        class="w-full mt-4 text-sm text-green-600 font-medium hover:text-green-800 transition-colors duration-200"
      >
        Ver todas las recolecciones
      </button>
    </div>
  </div>
</template>
<script setup lang="ts"></script>
