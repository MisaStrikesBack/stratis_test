# Stratis Zoo tech test

This the Stratis dev test

## Contents
* [Staging](#staging)
* [Api Docs](#api-docs)
* [Project setup](#project-setup)
* [Running development stack](#running-the-development-stack)
* [Halting development stack](#halting-development-stack)
* [Testing](#testing)
* [Code Quality](#code-quality)


### Staging

* **Heroku** - https://stratis-test.herokuapp.com/

### App Docs
- The small amount of time did not allow the creation of detailed documentation but this is an example of the documentation I use to do
* **Github docs** -  https://misastrikesback.github.io/places/ <-- Complete!

### Developer

| Name  | Contact |
| ------------- | ------------- |
| Misael Ramirez  | misaram89@gmail.com  |

## Development

### Project setup
- Cloning the repo:
```
$ git clone https://github.com/MisaStrikesBack/stratis_test.git
```
- Building the docker image using docker-compose
```
$ docker-compose build
```
- Migrating database
```
$ docker-compose run web python manage.py migrate
```
### Running the development stack
- Run in a terminal
```
$ docker-compose up web
```

### Halting development stack
- Run in a terminal
```
$ docker-compose up down
```
- Deleting database volume
```
$ docker-compose up down -v
```

### Testing
- The limited amount of time did not allow the creation of tests

- Runing python test suite
```
$ docker-compose run web python manage.py test
```
- Running specific test
```
$ docker-compose run web python manage.py test route.to.test.py
```

### Code Quality
- Running codeclimate
```
$ codeclimate analyze
```
- This project is checked with flake8

- Tox.init is also ready to be used with any continous integration tool
