FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Exposer le port utilisé par Flask
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]