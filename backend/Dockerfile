FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PTHONBUFFERRED 1
ENV APP_ENV dev

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8080
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]
