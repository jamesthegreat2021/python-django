from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/articles_list.html', {'articles': articles})

def article_detail(request,slug): 
   # return HttpResponse(slug)
   article = Article.objects.get(slug=slug)
   return render(request, 'articles/article_detail.html', {'article': article})

def article_create(request):
     
    return render(request, 'articles/article_create.html')