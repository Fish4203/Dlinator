from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
import random
import time
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

@login_required
def index(request): # index
    context = {}
    return render(request, 'index.html', context)

@login_required
def search(request, query): # index
    try:
        response = requests.get(f'http://192.168.20.69:9117/api/v2.0/indexers/all/results/torznab?t=search&q={query}&apikey={settings.JACKETT_TOKEN}')

        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.findAll('item')

        #print(items)

        results = []
        for item in items:
            # print('###################################')
            # print(item)
            # print(item.find('enclosure')['url'])
            seeders = 0
            for i in item.findAll('torznab:attr'):
                if 'seeders' in str(i):
                    seeders = i['value']

            cat = int(int(item.find('category').text) / 1000)
            if cat == 1:
                cat = 'Console'
            elif cat == 2:
                cat = 'Movie'
            elif cat == 3:
                cat = 'Audio'
            elif cat == 4:
                cat = 'PC'
            elif cat == 5:
                cat = 'TV'
            elif cat == 6:
                cat = 'XXX'
            else:
                cat = 'Other'

            mag = item.find('enclosure')['url']




            results.append({
                'title': item.find('title').text,
                'indexer': item.find('jackettindexer').text,
                'site': item.select('guid')[0].text,
                'date': item.select('pubdate')[0].text,
                'size': str(int(item.select('size')[0].text) / 1000000000),
                'mag': mag,
                'category': cat,
                'seeders': seeders,
            })

        context = {'results': results}
        return render(request, 'search.html', context)
    except Exception as e:
        return render(request, 'blank.html', {'error': e})


@login_required
def add(request): # index
    try:
        query = request.POST['query']
        title = request.POST['title']
        cat = request.POST['cat']
        # print('###############')
        # print(str(query))
        if 'magnet' not in query:
            try:
                magSite = requests.get(query)
            except Exception as e:
                query = str(str(e)[39:])[:-1]

        # print('maggggggggggggggggg')
        # print(query)

        f = open(f'{settings.PATH_TO_WATCH}{title}.magnet', 'w')
        f.write(query)
        f.close()

        context = {'title': title, 'loc': settings.PATH_TO_WATCH, 'mag': query}

        return render(request, 'done.html', context)
    except Exception as e:
        return render(request, 'blank.html', {'error': e})




def signin(request): # sign in function this shit is well writen so im not going to bother commenting
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('web:index')
        else:
            context = {'error_message': 'could not authentecate account'}
            return render(request, 'signin.html', context)

    elif request.method == 'GET':
        return render(request, 'signin.html')

@login_required
def new_account(request): # creates a new user function this shit is well writen so im not going to bother commenting

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()

            context = 'sucsessfuly created new account'
            return redirect('chat:index')#, error=context)
        except:
            context = {'error_message': 'could not created new account'}
            return render(request, 'new_account.html', context)

    elif request.method == 'GET':
        return render(request, 'new_account.html')


def signout(request):
    logout(request)
    return redirect('web:index')
