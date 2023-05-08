from django.shortcuts import render
from django.views.generic import ListView

from mall.models import Product


class ProductListView(ListView):
    model = Product
    product_qs = Product.objects.all().select_related("category")
    paginate_by = 4


product_list = ProductListView.as_view()
