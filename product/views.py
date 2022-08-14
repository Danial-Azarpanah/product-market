from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Comment


class ProductListView(ListView):
    """
    All products in paginated view
    """
    model = Product
    paginate_by = 2


def product_detail(request, slug):
    """
    Product detail
    """
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get("body")
        Comment.objects.create(product=product, user=request.user, body=body, parent_id=parent_id)
    return render(request, "product/product_detail.html", context={"product": product})

