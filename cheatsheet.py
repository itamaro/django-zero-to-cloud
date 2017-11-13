S22

consider live demo
http://docs.aws.amazon.com/lambda/latest/dg/get-started-create-function.html


S36

from __future__ import print_function

import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    """Demonstrates a simple HTTP endpoint using API gateway.
    You have full access to the request and response payload,
    including headers and status code.
    """
    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'all good!', 'message': 'Hello, Lambda!'}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

S43

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04


S48

pwd
whoami
uname -a
python -V
python3 -V
pip3 -V


S49

mkdir djproject && cd djproject
python3 -m venv djenv
source djenv/bin/activate
pip install django gunicorn psycopg2


S51

sudo -u postgres psql
CREATE DATABASE my_django;
CREATE USER my_dj_user WITH PASSWORD 'myStrongP@ssword!';
ALTER ROLE my_dj_user SET client_encoding TO 'utf8';
ALTER ROLE my_dj_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE my_dj_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE my_django TO my_dj_user;
\q


S52

mkdir djproject && cd djproject
python3 -m venv djenv
source djenv/bin/activate
pip install django gunicorn psycopg2


S54

gcloud compute copy-files multiapp test-vm-1:/home/itamar/djproject --zone us-east1-a


S55

ALLOWED_HOSTS = ['dj1.theostri.ch']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_django',
        'USER': 'my_dj_user',
        'PASSWORD': 'myStrongP@ssword!',
        'HOST': 'localhost',
        'PORT': '',
    }
}


S56

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


S57

python manage.py runserver 0.0.0.0:8000


S58

gunicorn --bind 0.0.0.0:8000 multiapp.wsgi:application


S59

sudo nano /etc/systemd/system/gunicorn.service

'''
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=itamar
Group=www-data
WorkingDirectory=/home/itamar/djproject/multiapp
ExecStart=/home/itamar/djproject/djenv/bin/gunicorn --workers 4 --bind unix:/home/itamar/djproject/djproject.sock multiapp.wsgi:application

[Install]
WantedBy=multi-user.target
'''

sudo systemctl start gunicorn
sudo systemctl enable gunicorn


S60

sudo nano /etc/nginx/sites-available/djproject

'''
server {
    listen 80;
    server_name dj1.ostrich.io;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/itamar/djproject/djproject.sock;
    }
}
'''

sudo ln -s /etc/nginx/sites-available/djproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
