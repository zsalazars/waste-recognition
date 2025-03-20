# Etapa de construcción
FROM node:18 AS build

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar todo el código fuente
COPY . .

# Construir la aplicación para producción
RUN npm run build

# Etapa de producción
FROM nginx:alpine

# Copiar los archivos construidos desde la etapa anterior
COPY --from=build /app/dist /usr/share/nginx/html

# Exponer el puerto 80 para servir la aplicación
EXPOSE 80

# Iniciar Nginx cuando el contenedor se ejecute
CMD ["nginx", "-g", "daemon off;"]
