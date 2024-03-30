
FROM python:3.8-alpine

#WORKDIR /usr/Esummit23-backend

ENV PYTHONBUFFERED 1

# install psycopg2 dependencies for postgres
RUN apk update \
    && apk add --no-cache \
        gcc \
        musl-dev \
        python3-dev \
        libffi-dev \
        openssl-dev \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        fribidi-dev \
        libpng-dev \
        libwebp-dev \
        postgresql-dev \
    && rm -rf /var/cache/apk/*



RUN pip install --upgrade pip \
  && pip install --upgrade setuptools \
  && pip install --upgrade pipenv  \
  && pip install --upgrade boto3 \
  && pip install --upgrade django-storages \
  && pip install gevent

#  && pip install psycopg2


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /usr/esummit23-backend
WORKDIR /usr/esummit23-backend

COPY . .

CMD ["sh", "-c", "python manage.py collectstatic --no-input;python manage.py migrate;gunicorn esummit.wsgi:application -b 0.0.0.0:9006 --timeout 60000 -c config.py  "]