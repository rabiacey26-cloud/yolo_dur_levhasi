# Temel Python imajını kullanıyoruz
FROM python:3.9-slim

# Görüntü işleme (OpenCV) için gereken Ubuntu/Linux bağımlılıkları
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Çalışma klasörümüzü ayarlıyoruz
WORKDIR /app

# Kütüphaneleri kopyalayıp kuruyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Modeller ve kodlar dahil her şeyi içeri kopyalıyoruz
COPY . .

# Konteyner çalıştığında ana kodu başlat
CMD ["python", "main.py"]