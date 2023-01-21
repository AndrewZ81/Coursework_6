FROM node:14.21.2-alpine3.16 as build
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN apk add --update python3 make g++ && rm -rf /var/cache/apk/*
RUN npm i
COPY . ./
RUN ls -la
CMD npm run build
