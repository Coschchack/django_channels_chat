FROM python:3.8.6-slim-buster

WORKDIR /chat
ENV PYTHONPATH .

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
