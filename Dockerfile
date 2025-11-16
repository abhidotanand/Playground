FROM python:3.14-slim
WORKDIR /app
COPY FastApi/ch1/ /app
RUN pip install --no-cache-dir "fastapi[standard]"
CMD ["fastapi", "dev", "/app/main.py", "--host", "0.0.0.0"]