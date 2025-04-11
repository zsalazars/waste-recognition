<template>
  <div class="mx-auto">
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold text-gray-800">Residuos</h1>
        <p class="text-gray-600 mt-1">Gestión de categorías de residuos y sus elementos</p>
      </div>

      <!-- Podría agregar un botón para crear nueva categoría aquí -->
      <button
        class="bg-emerald-600 text-white px-4 py-2 rounded-lg hover:bg-emerald-700 transition-colors flex items-center gap-2"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 4v16m8-8H4"
          />
        </svg>
        Nueva Categoría
      </button>
    </div>

    <!-- Estado de carga -->
    <div v-if="isLoading" class="flex justify-center items-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600"></div>
    </div>

    <!-- Estado de error -->
    <div
      v-else-if="error"
      class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6"
    >
      <div class="flex">
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
            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        <p>Error al cargar residuos: {{ error }}</p>
      </div>
    </div>

    <!-- Contenido principal -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="residuo in residuosByCategorias" :key="residuo.id">
        <ResiduoCard :residuo="residuo" @delete="deleteResiduo" />
      </div>
    </div>

    <!-- Estado vacío -->
    <div
      v-if="!isLoading && !error && residuosByCategorias.length === 0"
      class="flex flex-col items-center justify-center py-16 bg-gray-50 rounded-xl"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-16 w-16 text-gray-300 mb-4"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"
        />
      </svg>
      <h3 class="text-xl font-medium text-gray-700 mb-1">No hay residuos disponibles</h3>
      <p class="text-gray-500">Crea una nueva categoría para comenzar</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useResiduoStore } from '@/stores/residuoStore'
import ResiduoCard from '@/components/ResiduoCard.vue'

const residuoStore = useResiduoStore()
const { residuosByCategorias, isLoading, error } = storeToRefs(residuoStore)

const deleteResiduo = async (id: number) => {
  console.log(id)
}

onMounted(async () => {
  await residuoStore.getAllResiduos()
})
</script>

<style scoped>
/* Agregar estilos para la vista de residuos */
</style>
