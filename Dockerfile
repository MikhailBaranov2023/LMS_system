FROM python:3.11

WORKDIR /LMS_system

COPY ./reqirements.txt /LMS_system/

RUN pip install -r requirements.txt

COPY . .
