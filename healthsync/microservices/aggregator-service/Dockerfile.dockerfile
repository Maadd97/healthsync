FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY aggregator.py .

# The Aggregator may run as a scheduled job and 
# doesn't necessarily expose an HTTP port, but you can EXPOSE if needed
# EXPOSE 5003

# For a simple approach, the aggregator runs on container start:
CMD ["python", "aggregator.py"]
