# Temel Python imajı
FROM python:3.11-slim

# Çalışma dizini
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Varsayılan komut
CMD ["python", "main.py", "--help"]
