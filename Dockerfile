FROM sasaco/frontistr-python:latest

RUN mkdir -p /usr/src/app

COPY app/* /usr/src/app

# テスト用
COPY tmp/* /tmp

# 本番用
# COPY tmp/run.sh /tmp/run.sh

WORKDIR /tmp

CMD [ "run.sh" ]