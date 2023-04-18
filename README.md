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

![Screenshot from 2023-04-18 17-08-07](https://user-images.githubusercontent.com/33897492/232821984-808a7e62-4fef-4635-a109-ac826652801d.png)


## Update location demo

[Screencast from 04-18-2023 05:11:36 PM.webm](https://user-images.githubusercontent.com/33897492/232822605-0459ca76-2f61-4210-b7ca-e633d65e125c.webm)

## Marker pop

[Screencast from 04-18-2023 11:18:15 AM.webm](https://user-images.githubusercontent.com/33897492/232822266-7ac3ff5e-cf86-41d3-a9a8-10a2d3979d3a.webm)

