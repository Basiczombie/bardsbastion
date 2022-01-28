# syntax=docker/dockerfile:1
FROM python:3
LABEL Name="Bastion Server"
LABEL Version="0.0.1"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .
