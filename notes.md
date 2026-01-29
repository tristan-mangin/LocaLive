# Virtual Environment

## Initialize virtual environment

* `python -m venv env`
* if doesn't work `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Activate virtual environment   

* `.\env\Scripts\Activate.ps1`

## Install all dependencies

* Create `requirements.txt` outside of `env`
* List dependencies in this file
* `pip install -r requirements.txt`
* Move `requirements.txt` into Django project folder

## Dependencies Used here

* `django-cors-headers` - fix cross origin request issue
* `djangorestframework\simplejwt` - authentification
* `python-dotenv` - load environment variables

# Backend

## General Notes

* Django uses object relational mapping (ORM)
* Serializer converts python code or objects into JSON or vice versa for API

## Start django project

* `django-admin startproject backend`

## Make django app

* Change to project directory `cd backend`
* `python manage.py startapp api`

## Configure Settings

* Reference `configure settings` commit in repo
* All changes made in `settings.py`

# Frontend

