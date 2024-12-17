FROM mcr.microsoft.com/devcontainers/python:3.12

WORKDIR /computation_and_information

COPY . .

RUN export DEBIAN_FRONTEND=noninteractive
RUN sudo apt-get update
RUN sudo apt-get clean
RUN sudo rm -rf /var/lib/apt/lists/*

RUN pipenv install
