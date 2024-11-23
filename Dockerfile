FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev && \
    pip install --no-cache-dir opencv-python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .  .

CMD ["python", "app.py"]