FROM python:3.12-alpine

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libpq-dev \
    libffi-dev \
    postgresql-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE store.settings

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn store.wsgi:application --bind 0.0.0.0:8000"]

EXPOSE 8000
