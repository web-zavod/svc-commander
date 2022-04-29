FROM python:3.10

WORKDIR /app
ENV PYTHONPATH=/app/src
EXPOSE 5000
RUN mkdir -p src/

COPY requirements.txt requirements.txt
RUN pip install --default-timeout=1000 --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src/ src/

ENTRYPOINT ["python", "-u", "-m", "src"]
