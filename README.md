# Chess API

This is an api creation project using python from chess games. It aims to return information from old matches.

## Versions

    python=3.7.9
    

## Output

```json

```

## Setup

### Enviroment

Before starting the project, create a virtual environment. I recommend `virtualenv`, but you can use whatever you prefer.

Install `virtualenv`

```sh
> pip install virtualenv
```

Create a virtual environment in root.

```sh
> virtualenv venv
```

### Database

Create a file `.env` to set your project. This file must have:

`.env`

    SECRET_KEY=<YOU_SECRET_KEY_DJANGO>
    ENGINE=<YOUR_ENGINE(SQLSERVER:sql_server.pyodbc)>
    NAME=<YOU_DATABASE_NAME>
    HOST=<HOST_FOR_YOUR_DATABASE>

If your database must have a login and password, you must put the information here and change the `settings.py` file using the variables correctly.

`settings.py`
```py
DATABASES = {
    'default': {
        'ENGINE': config['ENGINE'],
        'NAME': config['NAME'],
        'USER': '', # <YOU_USER>
        'PASSWORD': '', # <YOU_PASSWORD>
        'HOST': config['HOST'],
        'PORT': ''
    }
}
```

In the folder `scripts_sql`, run thats scritps on SQLServer to create the tables in database.

Finally make migrate in this project to set the model in Django

```sh
> python manage.py makemigrations
```

```sh
> python manage.py migrate
```

## Super User

In Django it is necessary to create a super user to be able to have more freedom to manipulate the data tables, so I recommend creating one.

```sh
> py manage.py createsuperuser
```