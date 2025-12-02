FROM node:22 AS build
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/usr/src/app/.npm \
    npm set cache /usr/src/app/.npm && \
    npm ci
COPY . .
RUN npm run build

FROM nginx
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
EXPOSE 80
