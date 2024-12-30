FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expose port 5002 if you want to keep consistency 
# with your sample code
EXPOSE 5002

CMD ["python", "app.py"]
