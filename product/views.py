from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Product
