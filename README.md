CONTENTS
---------------------

 * Introduction
 * Requirements
 * Recommended modules
 * Installation & Configuration

<h2>Introduction</h2>
This project is my attempt to implement the TODO application using Django technology and PostgreSQL as database. This application implements the functions of viewing, adding, marking completed/uncompleted, editing and deleting tasks. The project implements a system of user accounts and relevant access rights.
<h5>You can see the result via <a href="https://django-to-do-zhlty.ondigitalocean.app">LINK</a></h5>

<h2>Requirements</h2>
> * django==4.0.2;
> * python >= 3.7;

<h2>Recommended modules</h2>
> * psycopg2==2.9.3;
> * django-storages==1.12.3;
> * dj-database-url;
> * boto3==1.20.53;
> * python-dotenv

<h2>Installation & Configuration</h2>
Before installing process, you have to be sure that Python and Git are installed on your device.
```shell
~$ mkdir temp && cd temp
~$ git clone <repo-name>.git
~$ cd DjangoToDO/
~$ python -m venv djangoenv
```
If you use package manager PIP try:
```shell
~$ source djangoenv/bin/activate # or run activate.ps1 with PowerShell in Win10)
~$ pip install -r requirements.txt
```
For Poetry you should run:
```shell
~$ poetry env use /full/path/to/python
~$ poetry install
```
Now lets configure a little bit our project:
You have to create DB into your local PostgresSQL and configure environment variables. Also you could use sqlite DB (fast run). For this, please overwrite DATABASE variable in settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Now you must setting other environment variables DEBUG
```shell
~$ export DEBUG=True;DEVELOPMENT_MODE=True
```
For using default Django's staticfiles manager, please comment this line into settings.py
```python
from .cdn.conf import * # comment this
```
Notice, functions that depend on E-Mail SMTP won't be work.
So let's complete our installation.
```shell
~$ python manage.py makemigrations && python manage.py migrate
~$ python manage.py createsuperuser # and follow the instructions//
~$ python manage.py runserver
```
