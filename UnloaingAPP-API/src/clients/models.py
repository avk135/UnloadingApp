from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Client(models.Model):
    name = models.CharField(max_length=148)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)


class UnLoading(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    details = models.TextField(default='', blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    alredy_paid = models.FloatField(default=0)
    workers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return 'ID-{} | {} {}, Цена: {}, Заплачено: {}'.format(self.id, self.client.name, self.date, self.price, self.alredy_paid)