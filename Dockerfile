FROM python:3.10-alpine
WORKDIR /app



# install system dependencies
RUN apt-get update && apt-get install -y \
    espeak\
    ffmpeg


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

