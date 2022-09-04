FROM ghcr.io/louis030195/gitpod-google-cloud:latest

RUN sudo apt update && sudo apt install -y nodejs npm && npm install @openapitools/openapi-generator-cli -g