FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV API_HOSTNAME=backend-server
ENV API_PORT=8001

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]