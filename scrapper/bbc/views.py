from django.shortcuts import render
from .scrapper import Scrapper
from threading import Thread
from .models import Article


def home(request, template_name='bbc/home.html'):

    data = {}
    data['articles'] = Article.objects.all()
    #print(f'Object Count {objs.count()}')
    return render(request, template_name, data)

def scrape(request):

    data = {}
    Thread(target=Scrapper().run, daemon=True).start()
    return render(request, 'bbc/scrape.html', data)

def article(request, id : int):
    data = {}
    data['article'] = Article.objects.get(id=id)
    return render(request, 'bbc/article.html', data)

