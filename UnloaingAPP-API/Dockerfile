FROM python:alpine3.15 as build

COPY requirements.txt .

# build dependencies for psycopg2
RUN apk add gcc musl-dev postgresql-dev

RUN pip install --prefix=/install -r requirements.txt

FROM python:alpine3.15 as production

# a runtime dependency for psycopg2
RUN apk add --no-cache libpq

COPY --from=build /install /usr/local
COPY src /usr/src/app
