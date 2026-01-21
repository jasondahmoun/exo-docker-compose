FROM node:20

WORKDIR /app

COPY backend/src ./src
COPY docker/backend.env .env

RUN npm init -y \
 && npm install express pg dotenv axios socks-proxy-agent

EXPOSE 5001

CMD ["node", "src/index.js"]
