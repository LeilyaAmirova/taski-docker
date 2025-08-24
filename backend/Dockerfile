FROM python:3.12

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip setuptools==68.2.2
RUN pip install --no-cache-dir gunicorn==23.0.0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Явно установите все возможные недостающие зависимости
RUN pip install --no-cache-dir \
    djangorestframework \
    django-cors-headers \
    psycopg2-binary

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
