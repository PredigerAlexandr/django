from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", "url_name": 'about'},
        {'title': "Добавить статью", "url_name": 'add_page'},
        {'title': "Обратная связь", "url_name": 'contact'},
        {'title': "Войти", "url_name": 'login'},
]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context={
        'cats':cats,
        'posts':posts,
        'menu':menu,
        'title':'Главаня страница',
        'cat_selected':0
    }
    return render(request,'women/index.html', context=context)

def about(request):
    posts = Women.objects.all()
    return render(request,'women/about.html', {'posts': posts, 'menu':menu, 'title':'О сайте'})

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_id):
    return HttpResponse(f'Отображение страницы поста:{post_id}')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts)==0:
        raise Http404()
    context = {
        'cats': cats,
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>page found error<h1>')
