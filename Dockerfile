FROM python:3.10-slim
WORKDIR /app



# install system dependencies
RUN apt-get update && apt-get install -y \
    espeak


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

