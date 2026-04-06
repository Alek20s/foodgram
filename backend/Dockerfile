FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .
COPY data/ /app/data/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodgram.wsgi"]