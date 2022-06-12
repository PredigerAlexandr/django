from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте','Добваить статью','Обратная связь','Войти']

def index(request):
    posts = Women.objects.all()
    return render(request,'women/index.html', {'posts': posts, 'menu':menu, 'title':'Главная страница'})

def about(request):
    posts = Women.objects.all()
    return render(request,'women/about.html', {'posts': posts, 'menu':menu, 'title':'О сайте'})

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>сатегория {catid}<h1><p>{request.GET}</p>')

def archive(request, year):
    if int(year) >2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Сейчас такой год<h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page found error<h1>')
