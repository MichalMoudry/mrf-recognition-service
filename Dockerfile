FROM python:3.11.4-slim
WORKDIR /recognition-service

RUN apt-get update \
  && apt-get -y install tesseract-ocr

COPY ./requirements.txt .
COPY ./src ./app

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]