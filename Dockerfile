FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
COPY photos /app/photos


CMD ["python", "app.py", "/app/photos/img.png"]