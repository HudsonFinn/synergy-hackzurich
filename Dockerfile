FROM python:3.8.14

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY run.py server.py createdata.py ./
ADD static ./static

CMD gunicorn --bind 0.0.0.0:$PORT server:app