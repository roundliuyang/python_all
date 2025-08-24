from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def index(request):
    # 返回主页视图
    return HttpResponse("欢迎来到主页")

def article_detail(request, id):
    # 展示某篇文章
    article = Article.objects.get(id=id)
    return render(request, 'article_detail.html', {'article': article})