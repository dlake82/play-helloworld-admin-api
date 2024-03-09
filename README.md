# play-helloworld-auth-api

플레이-헬로월드 장고 인증 서버

## 장고 프로젝트 생성 방법

```
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
```

## 슈퍼 유저 생성

```
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```
