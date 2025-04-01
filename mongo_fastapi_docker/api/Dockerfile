# Pull image
FROM python:3.8-slim-buster
# FROM python:3.13.0-alpine

# setup workdir same as said in docker compose
WORKDIR /code

# #   config env variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

#   install inside container
# RUN python3 -m pip3 install --upgrade pip3
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY my_requirements.txt requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# -- Port that FastAPI will be listening on inside the container
EXPOSE 8000
# EXPOSE ${API_PORT}

# COPY . ./code/
COPY . .


#   Healthcheck to monitor the application
# HEALTHCHECK CMD ["curl", "--fail", "http://localhost:8000", "||", "exit 1"]

#   command to exec
# ENTRYPOINT python ./main.py

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "${API_PORT}"]