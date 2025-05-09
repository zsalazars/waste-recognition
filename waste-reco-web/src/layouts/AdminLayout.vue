<template>
  <div class="flex">
    <!-- Sidebar -->
    <aside
      class="w-64 bg-gradient-to-b from-green-600 to-teal-700 text-white min-h-screen shadow-xl transition-all duration-300 hidden lg:block relative overflow-hidden"
    >
      <!-- Decorative pattern overlay -->
      <div class="absolute inset-0 opacity-5">
        <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
          <pattern
            id="pattern-circles"
            x="0"
            y="0"
            width="20"
            height="20"
            patternUnits="userSpaceOnUse"
          >
            <circle cx="10" cy="10" r="3" fill="currentColor"></circle>
          </pattern>
          <rect x="0" y="0" width="100%" height="100%" fill="url(#pattern-circles)"></rect>
        </svg>
      </div>

      <!-- Logo and Title Section -->
      <div
        class="py-6 px-4 border-b border-green-500/30 flex items-center justify-center space-x-3 relative"
      >
        <div class="h-10 w-10 bg-white rounded-full flex items-center justify-center shadow-md">
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
              d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
            />
          </svg>
        </div>
        <h2 class="text-xl font-semibold text-white">
          Waste<span class="font-bold">Recognition</span>
        </h2>
      </div>

      <!-- User Section -->
      <div class="p-4 border-b border-green-500/30 mb-2 relative">
        <div class="flex items-center space-x-3">
          <div
            class="h-9 w-9 bg-teal-200 text-teal-700 rounded-full flex items-center justify-center font-bold"
          >
            A
          </div>
          <div>
            <div class="text-sm font-medium text-white">Admin Usuario</div>
            <div class="text-xs text-green-200">Administrador</div>
          </div>
        </div>
      </div>

      <!-- Navigation -->
      <nav class="p-4 relative">
        <h3 class="text-xs font-semibold text-green-200 uppercase tracking-wider mb-3 pl-3">
          Gestión Principal
        </h3>
        <ul class="space-y-2">
          <li>
            <RouterLink
              to="/dashboard"
              class="flex items-center py-2 px-3 rounded-lg text-green-100 hover:bg-white/10 transition-colors duration-200 group"
              active-class="bg-white/20 text-white font-medium shadow-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-3 text-green-300 group-hover:text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
                />
              </svg>
              Dashboard
            </RouterLink>
          </li>
          <li>
            <RouterLink
              to="/usuarios"
              class="flex items-center py-2 px-3 rounded-lg text-green-100 hover:bg-white/10 transition-colors duration-200 group"
              active-class="bg-white/20 text-white font-medium shadow-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-3 text-green-300 group-hover:text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
              Usuarios
            </RouterLink>
          </li>
          <li>
            <RouterLink
              to="/residuos"
              class="flex items-center py-2 px-3 rounded-lg text-green-100 hover:bg-white/10 transition-colors duration-200 group"
              active-class="bg-white/20 text-white font-medium shadow-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-3 text-green-300 group-hover:text-white"
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
              Residuos
            </RouterLink>
          </li>
          <li>
            <RouterLink
              to="/predicciones"
              class="flex items-center py-2 px-3 rounded-lg text-green-100 hover:bg-white/10 transition-colors duration-200 group"
              active-class="bg-white/20 text-white font-medium shadow-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-3 text-green-300 group-hover:text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path d="M4 14l4-4 4 4 8-8" />
                <path d="M4 20h16" />
                <path d="M6 16v4" />
                <path d="M10 12v8" />
                <path d="M14 16v4" />
                <path d="M18 8v12" />
                <circle cx="18" cy="5" r="2" />
              </svg>
              Predicciones
            </RouterLink>
          </li>
          <li>
            <RouterLink
              to="/reportes"
              class="flex items-center py-2 px-3 rounded-lg text-green-100 hover:bg-white/10 transition-colors duration-200 group"
              active-class="bg-white/20 text-white font-medium shadow-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-3 text-green-300 group-hover:text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                />
              </svg>
              Reportes
            </RouterLink>
          </li>
        </ul>

        <h3 class="text-xs font-semibold text-green-200 uppercase tracking-wider mb-3 mt-6 pl-3">
          Configuración
        </h3>
        <ul class="space-y-2">
          <li>
            <RouterLink
              to="/ajustes"
              class="flex items-center py-2 px-3 rounded-lg text-green-100 hover:bg-white/10 transition-colors duration-200 group"
              active-class="bg-white/20 text-white font-medium shadow-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-3 text-green-300 group-hover:text-white"
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
              Ajustes
            </RouterLink>
          </li>
          <li>
            <RouterLink
              to="/"
              @click.prevent="logout"
              class="flex items-center py-2 px-3 rounded-lg text-green-100 hover:bg-white/10 hover:text-red-100 transition-colors duration-200 group"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 mr-3 text-green-300 group-hover:text-red-100"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                />
              </svg>
              Cerrar Sesión
            </RouterLink>
          </li>
        </ul>
      </nav>

      <!-- Footer -->
      <div class="absolute bottom-0 left-0 right-0 p-4 border-t border-green-500/30">
        <div class="flex items-center justify-center space-x-1 text-xs text-green-200">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <span>v1.2.0</span>
        </div>
      </div>
    </aside>

    <!-- Mobile Toggle Button -->
    <div class="fixed bottom-4 right-4 lg:hidden z-50">
      <button
        @click="toggleSidebar"
        class="bg-green-600 hover:bg-green-700 text-white h-12 w-12 rounded-full flex items-center justify-center shadow-lg focus:outline-none"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            v-if="sidebarOpen"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          />
        </svg>
      </button>
    </div>

    <!-- Mobile Sidebar (Hidden by default) -->
    <aside
      v-show="sidebarOpen"
      class="fixed inset-0 bg-gradient-to-b from-green-600 to-teal-700 text-white z-40 lg:hidden transform transition-transform duration-300"
      :class="sidebarOpen ? 'translate-x-0' : '-translate-x-full'"
    >
      <!-- Mobile sidebar content (duplicate of desktop sidebar) -->
      <!-- ... same content as desktop sidebar ... -->
    </aside>

    <!-- Main Content -->
    <div class="flex-1">
      <!-- Top Header -->
      <header class="bg-white shadow-sm">
        <div class="mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between h-16">
            <div class="flex items-center">
              <button
                @click="toggleSidebar"
                class="p-2 lg:hidden rounded-md text-gray-700 hover:bg-gray-100 focus:outline-none"
              >
                <svg
                  class="h-6 w-6"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 6h16M4 12h8m-8 6h16"
                  />
                </svg>
              </button>
              <h1 class="ml-2 text-xl font-semibold text-gray-800">Dashboard</h1>
            </div>

            <div class="flex items-center">
              <div class="relative">
                <button class="p-1 text-gray-600 hover:text-gray-800 focus:outline-none">
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
                      d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                    />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </header>

      <!-- Page Content -->
      <main class="p-6">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const sidebarOpen = ref(false)

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value
}

const logout = () => {}
</script>
