# UnloaingAPP-API

API for mobile app to control shipment of goods.
The mobile app is [here](https://github.com/Vlad202/UnloaingAPP/)

There are some needed environment variables: 
- POSTGRES_NAME - name of a database;
- POSTGRES_USER - username of a database user;
- POSTGRES_PASSWORD - user's password;
- POSTGRES_HOST - database hostname;
- POSTGRES_PORT - database port;
- DJANGO_DEBUG - debugging in django, `TRUE` or `FALSE`.

## Deployment

Prerequisites:
 - ubuntu instance;
 - set up jenkins server with credentials and a pipeline reffered to `Jenkinsfile`;
