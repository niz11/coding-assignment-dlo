FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# Command to run the script (or Flask server)
CMD ["python3", "server.py"]