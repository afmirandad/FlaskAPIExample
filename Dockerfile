# Dockerfile para despliegue en Railway
FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
