FROM node
LABEL Name="client"
LABEL Version="0.0.1"
WORKDIR /client
ENV PATH /app/node_modules/.bin:$PATH
COPY package*.json .
RUN export NODE_OPTIONS=--openssl-legacy-provider
RUN npm install --silent
RUN npm install react-scripts@5.0.0 -g --silent
COPY ./ .
