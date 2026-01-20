FROM python:3.12-slim

WORKDIR /app
RUN pip install flask flask-cors

COPY back.py .

EXPOSE 5000
CMD ["python", "back.py"]