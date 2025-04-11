<template>
  <div
    class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100"
  >
    <!-- Encabezado con ícono -->
    <div class="bg-emerald-600 p-4 rounded-t-xl flex items-center justify-between">
      <h2 class="text-xl font-bold text-white">{{ props.residuo.nombre }}</h2>
      <div class="bg-white p-2 rounded-full">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 text-emerald-600"
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
    </div>

    <!-- Contenido -->
    <div class="p-5">
      <!-- Contador de elementos -->
      <div class="flex justify-between mb-3">
        <span class="text-sm text-gray-500">Elementos en categoría</span>
        <span class="bg-emerald-100 text-emerald-800 px-2 py-1 rounded-full text-xs font-medium">
          {{ props.residuo.residuos.length }}
        </span>
      </div>

      <!-- Lista de residuos -->
      <div class="max-h-48 overflow-y-auto pr-2 mb-4">
        <div
          v-for="item in props.residuo.residuos"
          :key="item.id"
          class="py-2 px-3 mb-2 bg-gray-50 rounded-lg flex items-center hover:bg-gray-100 transition-colors"
        >
          <div class="w-2 h-2 rounded-full bg-emerald-500 mr-3"></div>
          <p class="text-gray-700 font-medium">{{ item.nombre }}</p>
        </div>
      </div>

      <!-- Botón de eliminar -->
      <div class="flex justify-end pt-2 border-t border-gray-100">
        <button
          @click="emit('delete', props.residuo.id)"
          class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors flex items-center gap-2"
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
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
            />
          </svg>
          Eliminar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { ResiduoCategoria } from '@/models/Residuo'

const props = defineProps<{
  residuo: ResiduoCategoria
}>()

const emit = defineEmits<{
  (e: 'delete', id: number): void
}>()
</script>
