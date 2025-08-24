from django.db import models

from django.db import models
from django.db.models import ForeignKey


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    publisher = ForeignKey(Publisher, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# 一对一，一对多