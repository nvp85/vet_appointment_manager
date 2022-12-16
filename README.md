
## vet_appointment_manager

### Introduction

This is a learning project I made during Nucamp coding bootcamp course "Modern Software Engineering with DevOps".
It's a simplified appointment manager with API for an imaginary veterinary clinic created with Django REST framework and Postgresql.

### General Info

API end-points:
|url|methods|description|
|---|-------|-----------|
|/clients/|GET, POST|get a list of clients, add a new client|
|/clients/:id|GET, PATCH, DELETE|get a client by id, update a client by id, delete a client by id|
|/pets/ |GET, POST | get a list of pets, add a new pet|
|/pets/:id |GET, PATCH, DELETE | get a pet by id, update a pet by id, delete a pet by id|
|/specialists/ |GET, POST|get a list of specialists, add a new specialist|
|/specialists/:id |GET, PATCH, DELETE|get a specialist by id, update a specialist by id, delete a specialist by id|
|/appointments/|GET, POST|get a list of appointments, add a new appintment|
|/appontments/:id |GET, PATCH, DELETE|get an appointment by id, update an appointment by id, delete an appointment by id|

### Technologies

Python 3.9

Django 4.0.2

djangorestframework 3.13.1

psycopg2 2.9.3

(the full list is in requirements.txt)

### Launch

Prerequisites: python 3.7+, git, Postgresql 13+ running on the port 5432 (default port).

To run this project locally implement following:

* Clone the repository
```
$ git clone https://github.com/nvp85/vet_appointment_manager.git
```
* Set up and activate a virtual environment
```
$ python -m venv venv
$ source venv/bin/activate (or . Scripts/activate for Windows)
```
* Install requirements.txt
```
$ pip install -r requirements.txt 
```
* Create a database
```
$ psql -U postgres
postgres=# CREATE DATABASE appointment_manager
```
* Create .env file and put your postgres credentials in it. Exemplary content of an .env file:
```
# Database Settings
DB_NAME=appointment_manager
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=127.0.0.1
DB_PORT=5432
# Secret key
SECRET_KEY = 'your-secret-key'
DEBUG = True
```
* Generate a new secret key and put it in .env file
```bash
$ python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```

* Make migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
* Create a new superuser 
```
$ python manage.py createsuperuser --username your_username --email mail@example.com
```
* The project uses token auth. So create a token:
```
$ python manage.py drf_create_token <your_username>
$ ./manage.py drf_create_token <your_username>
```
>For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

>Authorization: Token  98dfe578bb0c891a4590d044956ea8fa21d512d4"

* Start the development server
```
$ python manage.py runserver
```
