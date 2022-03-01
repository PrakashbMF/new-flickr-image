# new-flickr-image

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
    $ git clone https://github.com/PrakashbMF/new-flickr-image.git
    $ cd new-flickr-image
```

Create a virtual environment to install dependencies in and activate it:

```sh
    ~/new-flickr-image$ virtualenv -p python3.8 env
    ~/new-flickr-image$ source env/bin/activate
```

```sh
    (env) ~/new-flickr-image$ pip3 install -r requirements.txt
```

# .env file

```sh 
    find the env.template file in BASE DIR path and convert it into .env file by name change to .env
    and provide value per key included in that.
    
```

# Database

```sh 
    Also provide Database details in .env file then you can makemigrations and migrate like just below command.
```

# Migration DB Model

```sh
    (env) ~/new-flickr-image$ python3 manage.py makemigrations
    (env) ~/new-flickr-image$ python3 manage.py migrate
```

# For Admin panel

Create a Superuser to check Database by providing username,email(optional),password

```sh
    (env) ~/new-flickr-image$ python3 manage.py createsuperuser

```

## Starting the web server

```sh
    (env) ~/new-flickr-image$ python manage.py runserver 8000
```

## on Browser navigate to

```sh
    http://127.0.0.1:8000/signup/
```

## To access Admin panel

```sh 
    http://127.0.0.1:8000/admin/
```

## Project diagram

```sh
    new-flickr-image
    ├── manage.py
    ├── new-flickr-image
    │     └── ...
    ├── myapp
    │  ├── migrations
    │  ├── static
    │  │  ├── myapp
    │  │  │  ├── homeStyle.css
    │  │  │  ├── signup.css
    │  │  │  └── style.css
    │  ├── templates
    │  │  ├── myapp
    │  │  │  ├── favourite.html
    │  │  │  ├── favremovejs.html
    │  │  │  ├── home.html
    │  │  │  ├── homejs.html
    │  │  │  ├── searchjs.html
    │  │  │  ├── signin.html
    │  │  │  ├── signinjs.html
    │  │  │  ├── signup.html
    │  │  │  └── signupjs.html
    │  ├── util
    │  │  ├── flick_api.py
    │  │  └──  service.py
    │  ├── __init__.py
    │  ├── admin.py
    │  ├── apps.py
    │  ├── data_serializer.py
    │  ├── forms.py
    │  ├── managers.py
    │  ├── models.py
    │  ├── tests.py
    │  ├── urls.py
    │  └── views.py
    ├── gitignore
    ├── env.template
    ├── README.md
    └── requirements.txt
```