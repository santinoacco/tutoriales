# Pull image
FROM python:3.8-slim-buster

# setup workdir same as said in docker compose
WORKDIR /code
# -- Install inside container
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# -- Port that FastAPI will be listening on inside the container
EXPOSE 8000

COPY . .

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]