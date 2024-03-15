FROM python:3.10-alpine

RUN set -eux; \
    sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && apk add  --no-cache gcc libc-dev linux-headers make pcre-dev zlib-dev openssl-dev libffi-dev musl-dev python3-dev \
    && pip install uwsgi \
    && pip install flask
