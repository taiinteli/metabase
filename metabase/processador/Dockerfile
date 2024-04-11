FROM python:3.9

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y wait-for-it

RUN pip install --no-cache-dir -r requirements.txt

CMD wait-for-it hivemq:1883 -- python ./processador.py