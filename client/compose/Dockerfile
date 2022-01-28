FROM node
LABEL Name="Bastion Client"
LABEL Version="0.0.1"
WORKDIR /webui
ENV PATH /app/node_modules/.bin:$PATH
COPY ./webui/package*.json .
RUN export NODE_OPTIONS=--openssl-legacy-provider
RUN npm install --silent
RUN npm install react-scripts@4.0.3 -g --silent
COPY ./webui .
