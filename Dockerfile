FROM python:3.11.4-slim-buster
WORKDIR /recognition-service

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./src ./app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]