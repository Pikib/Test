from django.shortcuts import render
from django.views import generic
from products import models


class ProductsView(generic.ListView):
    model = models.Products
    render(model, template_name='products.html')
# Create your views here.
