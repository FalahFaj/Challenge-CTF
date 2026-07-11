FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY templates ./templates
COPY unej.html .
COPY app.py .

RUN useradd -m ikantuk
USER ikantuk

EXPOSE 5000

CMD ["python", "app.py"]