# syntax=docker/dockerfile:1
FROM python:3.8-alpine3.14
ADD . /pypotter-books-docker-dir
WORKDIR /pypotter-books-docker-dir
RUN apk add --no-cache gcc g++ # sqlalchemy package dependencies
RUN apk add --no-cache mariadb-dev mariadb-client # mysqlclient package dependencies
RUN apk add --no-cache git # pre-commit package dependency
RUN pip install -r requirements-dev.txt
RUN git init
EXPOSE 5000
# CMD ["python3", "manage.py", "runserver", "--host", "0.0.0.0"] # TODO: pending to define a production Dockerfile
CMD ["flask", "run", "--host", "0.0.0.0"]
