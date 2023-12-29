FROM python:3.10-slim
WORKDIR /app


# install system dependencies
RUN apt-get update && apt-get install -y \
    espeak \
    ffmpeg


# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt /app/
RUN pip3 install -r requirements.txt


COPY . /app

