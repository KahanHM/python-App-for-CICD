# Stage 1: Build the application
FROM python:3.9 AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Run the application (Distroless)
FROM gcr.io/distroless/python3

WORKDIR /app
COPY --from=builder /app /app

CMD ["main.py"]
