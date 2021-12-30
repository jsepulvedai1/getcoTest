# getcoTest-backend


_prueba tecnica Django._

[[_TOC_]]

## Comenzando 🚀

Desarrollado con python 3.9.7, Django y Postgresql


## Pre-requisitos 📋
* [python](https://www.python.org/downloads/release/python-390/)
* [Django](https://www.djangoproject.com/download/)
* [Postgresql](https://www.postgresql.org/)


### Dependencies

Next install the app dependencies with python.

```bash
# If you use pip
pip install -r requirements.txt

# If you use pip3
pip3 install -r requirements.txt
```

_para levantar la bd de manera local utilizaremos docker-compose de la siguiente forma:_

```
docker-compose up -d
```


_A continuación, para levantar la api, lanzaremos el siguiente comando:._

```
python manage.py migrate
python manage.py runserver
```

## Test
_Para realizar test, lanzaremos el siguiente comando:._

```
python manage.py test
```
## Endpoints

- list_travels
- register
- auth/login
- user_travels/id
- user_travels/id/categories/1


