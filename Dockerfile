FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    git \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/ultralytics/yolov5.git
WORKDIR /app/yolov5
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir streamlit
COPY . /app/
EXPOSE 8501
CMD ["streamlit", "run", "yolov5/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
