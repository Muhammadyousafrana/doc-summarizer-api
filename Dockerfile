# Use a Python base image with FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Set the working directory
WORKDIR /app

# Install system dependencies (FFmpeg + additional packages for textract and other tools)
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    antiword \
    unrtf \
    poppler-utils \
    tesseract-ocr \
    flac \
    ffmpeg \
    lame \
    libmad0 \
    libsox-fmt-mp3 \
    sox \
    libjpeg-dev \
    swig && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Downgrade pip (to avoid pip v24+ issues with certain packages)
RUN pip install --no-cache-dir "pip<24.0"

# Copy the application code and dependencies
COPY main.py /app/
COPY requirements.txt /app/
COPY my_lib /app/my_lib

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
