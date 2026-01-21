FROM node:20

WORKDIR /app

COPY frontend/src ./src
COPY docker/frontend.env .env

RUN npm init -y
RUN npm install express dotenv axios

EXPOSE 3000

CMD ["node", "src/index.js"]
