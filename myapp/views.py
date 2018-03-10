from django.shortcuts import render
from django.http import HttpResponse, Http404
from myapp.models import Product, Article
from django.template.loader import get_template
import random

# Product
def about(request):
    template = get_template('about.html')
    html = template.render()

    return HttpResponse(html)

def listing(requeset):
    products = Product.objects.all()
    template = get_template("list.html")
    html = template.render({'products': products})

    return HttpResponse(html)

def disp_detail(request, name):

    try:
        p = Product.objects.get(name = name)
    except Product.DoesNotExist:
        raise Http404('找不到指定产品')
    template = get_template("disp.html")
    html = template.render({'product': p})

    return HttpResponse(html)

def index(request):
    template = get_template("index.html")
    quotes = ['今日事,今日毕','知识就是力量']
    html = template.render({'quote': random.choice(quotes)})

    return HttpResponse(html)

# Article
def disp_article(request, tag):

    try:
        article = Article.objects.get(tag = tag)
    except Article.DoesNotExist:
        raise Http404("找不到指定文章")
    template = get_template("disp_article.html")
    html = template.render({'article': article})

    return HttpResponse(html)

def list_article(request):
    articles = Article.objects.all()
    template = get_template("list_article.html")
    html = template.render({'articles': articles})

    return HttpResponse(html)

def post(request, post_date):
    html = "<h2>Post Data is {}</h2><hr>".format(post_date)
    return HttpResponse(html)
