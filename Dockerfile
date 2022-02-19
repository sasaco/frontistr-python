FROM sasaco/frontistr-python:latest

WORKDIR /tmp

COPY app/* /tmp
COPY tmp/* /tmp

CMD [ "run.sh" ]