from .models import Article

# 增

# 方法一：save方法
def article_save():
    article = Article(title="My first article", body="My first article body")
    article.save()

# 方法二：create方法
def article_create():
    article = Article.objects.create(title="My first article", body="My first article body")

# 方法三：bulk_create方法


# 删

# 删除单条数据
def task_delete_one():
    Article.objects.get(pk=5).delete()

# 改
def article_save2():
    article = Article.objects.get(id=1)
    article.title = "New article title"
    article.save()


 # 查
def article_query():
    # QuerySet类型，实例对象列表
    Article.objects.all()
    # 字典列表
    Article.objects.all().values()
    # 只获取title-字典形式
    Article.objects.all().values('title')
    # 只获取title列表- 元组形式，只有value，没有key
    Article.objects.all().values_list('title')
    # 只获取title列表，只有value
    Article.objects.all().values_list('title', flat=True)