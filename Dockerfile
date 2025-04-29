# Base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only required project files
COPY requirements.txt ./requirements.txt
COPY app/ ./app/
COPY Models/ ./Models/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app/app.py"]
