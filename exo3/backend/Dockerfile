FROM python:3.12-slim

WORKDIR /app

# requests + support SOCKS (PySocks)
RUN pip install flask flask-cors requests[socks]

COPY back.py .

EXPOSE 5000
CMD ["python", "back.py"]