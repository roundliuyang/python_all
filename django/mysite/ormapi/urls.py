# tasks/urls.py
from django.urls import  path, re_path
from . import views

# namespace
app_name = 'ormapi'

urlpatterns = [
    path('blog/', views.index),
    path('blog/articles/<int:id>/', views.article_detail, name='article_detail'),
    re_path(r'^blog/articles/(?P<id>\d+)/$', views.article_detail, name='article_detail'),
]