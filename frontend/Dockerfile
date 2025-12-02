# Build Angular app
FROM node:22 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Serve using nginx
FROM nginx:1.25
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
EXPOSE 80
