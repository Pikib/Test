from django.db import models

# Create your models here.

from django.db import models
from django import forms


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    weight = models.IntegerField(verbose_name='Вес')
    material = models.CharField(max_length=50, verbose_name='Материал')
    manufacturer = models.ForeignKey('Manufacturers',
                                     verbose_name='Изготовитель',
                                     on_delete=models.CASCADE,
                                     )


    def __str__(self):
        return self.name




class Manufacturers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.name
