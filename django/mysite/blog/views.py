from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .forms import ArticleForm
from .models import Article


# 展示所有文章
def index(request):
    latest_articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog/article_list.html', {"latest_articles": latest_articles})

# 展示所有文章
def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'blog/article_detail.html', {"article": article})

    # 创建文章


def article_create(request):
    # 如果用户通过POST提交，通过request.POST获取提交数据
    if request.method == "POST":
        # 将用户提交数据与ArticleForm表单绑定
        form = ArticleForm(request.POST)
        # 表单验证，如果表单有效，将数据存入数据库
        if form.is_valid():
            form.save()
            # 创建成功，跳转到文章列表
            return redirect(reverse("blog:article_list"))
    else:
        # 否则空表单
        form = ArticleForm()
    return render(request, "blog/article_form.html", {"form": form, })

    # 更新文章


def article_update(request, pk):
    # 从url里获取单篇文章的id值，然后查询数据库获得单个对象实例
    article = get_object_or_404(Article, pk=id)

    # 如果用户通过POST提交，通过request.POST获取提交数据
    if request.method == 'POST':
        # 将用户提交数据与ArticleForm表单绑定，进行验证
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            # 更新成功，跳转到文章详情
            return redirect(reverse("blog:article_detail", args=[pk, ]))
    else:
        # 否则用实例生成表单
        form = ArticleForm(instance=article)

    return render(request, "blog/article_form.html", {"form": form, "object": article})


# 前面案例中的index，article_detail和article_update的方法都是基于函数的视图。函数视图的优点是比较直接，容易读者理解, 缺点是不便于继承和重用。
# 基于类的视图以class定义，而不是函数视图的def定义。使用类视图后可以将视图对应的不同请求方式以类中的不同方法来区别定义(get方法处理GET请求，post方法处理POST请求)，
# 相对于函数视图逻辑更清晰，代码也有更高的复用性。
class MyClassView(View):
    """类视图"""
    def get(self, request):
        """处理GET请求"""
        return render(request, 'register.html')

    def post(self, request):
        """处理POST请求"""
        return ...