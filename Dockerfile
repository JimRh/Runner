FROM python:3


RUN apt-get update && apt-get install -y g++

COPY . /App

WORKDIR /App

CMD ["bash","shell.sh"]