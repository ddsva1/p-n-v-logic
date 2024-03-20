FROM ubuntu:latest
MAINTAINER ddsva1 shani.desilva@student.manchester.ac.uk
RUN apt-get update
RUN apt-get install curl
RUN apt install -y iputils-ping python3
run apk add python3 py3-pip
run pip3 install flask flask-restful
run mkdir /folder
COPY ./app.py ./folder/app.py
CMD python3 ./sharedfolder/proof/proof.py