# Dlinator

## About
This is a simple site that searches Jackett for torrents and then based on the category adds .magnet files to a watch folder.

it is written in Django

## how to use

Make a config.env file in the same folder as manage.py

```
{ "SECRET_KEY":"key", "DEBUG": false, "JACKETT_IP": "192.168.???.???", "JACKETT_TOKEN":"token", "PATH_TO_WATCH":"", "ALLOWED_HOSTS":[]}


```


then find some way to host the django server

gunicorn dlinatorr.wsgi -b :8085 -D
