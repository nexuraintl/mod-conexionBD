FROM python:3.11-slim

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run escucha en el puerto 8080 por defecto
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app