# Profiles App
A small django application to list user and their locations on the map.


### Setup

## Installation on Linux and Mac OS

You need to install install postgresql or get an instance from AWS or Heroku.

You can folow the instraction from [here](https://www.postgresql.org/download/).


* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

```
$ virtualenv --python=python3 myvenv

$ source myvenv/bin/activate

(myvenv) $ pip install -r requirements.txt

(myvenv) $ python manage.py makemigrations

(myvenv) $ python manage.py migrate

(myvenv) $ python manage.py runserver locahlost:8000

```

## API Keys

You are only required to have one API key for google maps
you can get it from [here](https://developers.google.com/maps/documentation/javascript/get-api-key).

Update the `.env` file following the `.env.example`

## To access app on 

`http://localhost:8000/`

## Register an account

http://localhost:8000/accounts/register/

## View profile

http://localhost:8000/accounts/map/


## Access admin and and login super user

Access the admin interface at http://localhost:8000/admin/ and log in with the superuser account created in

```
# Create a super user account

python manage.py createsuperuser

```

Then you can add staff users with the permission level as per your requirements.


## Screenshots
