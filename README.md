# Dlinator

## About
This is a simple site that searches Jackett for torrents and then based on the category adds .magnet files to a watch folder.

it is written in Django

## how to use

Make a config.env file in the same folder as manage.py

```
SECRET_KEY=put some this secure here
DEBUG=False
JACKETT_IP='address of the jacket server'
JACKETT_TOKEN='the token you get from jackett'
PATH_TO_WATCH='the absolute path to you watch folder'



```


then find some way to host the django server
