FROM nginx:latest

# Copiar configuración personalizada de Nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80 dentro del contenedor
EXPOSE 80
