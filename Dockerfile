FROM python:3.10

WORKDIR /app
ENV PYTHONPATH=/app/scr
EXPOSE 5000
RUN mkdir -p scr/

COPY requirements.txt requirements.txt
RUN pip install --default-timeout=1000 --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY scr/ scr/

ENTRYPOINT ["python", "-u", "-m", "scr"]