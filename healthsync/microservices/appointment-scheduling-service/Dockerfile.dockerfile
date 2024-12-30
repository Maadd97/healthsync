FROM python:3.9-slim

WORKDIR /app

# 1. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy all source code, including app.py and the templates folder
COPY app.py .
COPY templates/ templates/

# 3. Expose port 5001 (if you’re still using that port)
EXPOSE 5001

# 4. Start the Flask app (development server for simplicity)
CMD ["python", "app.py"]
