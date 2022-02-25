# flickrImage
# image-platform

```sh
    We're going to create a small blog! 
    1.do sign up 
    2.do login with your credential
    3.for images search by location name or (longitude and latitude together)
    4.you can add images to your favourite list
```

## SETUP

The first thing to do is to clone the repository:

```sh
    $ git clone https://github.com/PrakashbMF/imagePlatform.git
    $ cd imagePlatform
```

Create a virtual environment to install dependencies in and activate it:

```sh
    ~/imagePlatform$ virtualenv -p python3.8 env
    ~/imagePlatform$ source env/bin/activate
```

```sh
    (env) ~/imagePlatform$ pip3 install -r requirements.txt
```

# Migration DB Model

```sh
    (env) ~/imagePlatform$ python3 manage.py makemigrations
    (env) ~/imagePlatform$ python3 manage.py migrate
```

# For Admin panel

Create a Superuser to check Database by providing username,email(optional),password

```sh
    (env) ~/imagePlatform$ python3 manage.py createsuperuser

```

## Starting the web server

```sh
    (env) ~/imagePlatform$ python manage.py runserver 8000
```

## on Browser navigate to

```sh
    http://127.0.0.1:8000/platform
```

## To access Admin panel

```sh 
    http://127.0.0.1:8000/admin/
```

## Project diagram

```sh
    imagePlatform
    ├── manage.py
    ├── imagePlatform
    │     └── ...
    ├── myapp
    │  ├── flickr
    │  │  ├── __init__.py
    │  │  ├── flickr_api.py
    │  │  └── flickr_data.py
    │  ├── migrations
    │  ├── services
    │  │  ├── favourite_service.py
    │  │  ├── geo_location_service.py
    │  │  ├── location_service.py
    │  │  └── user_service.py
    │  ├── static
    │  │  ├── myapp
    │  │  │  ├── style.css
    │  │  │  └── welcomeStyle.css
    │  ├── template
    │  │  ├── myapp
    │  │  │  ├── favourites.html
    │  │  │  ├── home.html
    │  │  │  └── signup.html
    │  ├── views_file
    │  │  ├── favourite_view.py
    │  │  ├── home_view.py
    │  │  ├── image_view.py
    │  │  ├── location_view.py
    │  │  ├── platform_view.py
    │  │  └── user_view.py
    │  ├── __init__.py
    │  ├── admin.py
    │  ├── apps.py
    │  ├── data_serializer.py
    │  ├── models.py
    │  ├── tests.py
    │  ├── urls.py
    │  └── views.py
    ├── env
    │  └── ...
    ├── gitignore
    ├── README.md
    └── requirements.txt
```