From python:3.9-slim

RUN pip install FLASK prometheus-flask-exporter

WORKDIR /app

COPY pythonserver.py .

EXPOSE 8080

CMD ["python", "pythonserver.py"]