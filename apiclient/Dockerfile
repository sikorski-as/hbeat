FROM python:3.7-alpine
WORKDIR /opt
COPY . /opt
RUN pip install -r requirements.txt
CMD [ "python", "./daemon.py" ]