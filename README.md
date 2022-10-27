
## vet_appointment_manager

### Introduction

This is a learning project I made during Nucamp coding bootcamp course "Modern Software Engineering with DevOps".
It's an API of a simplified appointment manager for an imaginary veterinary clinic created with Django REST framework and Postgresql.

### General Info

API end-points:

/clients/ - GET a list of clients, POST - add a new client

/clients/:id - GET one particular client by id, PATCH - update a client by id, DELETE a client by id

/pets/ - GET a list of pets, POST - add a new pet

/pets/:id - GET one pet by id, PATCH - update a pet by id, DELETE a pet by id

/specialists/ - GET a list of specialists, POST - add a new specialist

/specialists/:id - GET a specialist by id, PATCH - update a specialist by id, DELETE a specialist by id

/appointments/ - GET a list of appointments, POST - add a new appintment

/appontments/:id - GET an appointment by id, PATCH - update an appointment, DELETE an appointment by id

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
$ psql
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
