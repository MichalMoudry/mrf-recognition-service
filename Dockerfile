FROM python:3.11.4-slim
WORKDIR /recognition-service

RUN apt-get update \
  && apt-get -y install tesseract-ocr

COPY ./requirements.txt .
COPY ./src ./app