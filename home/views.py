from django.shortcuts import render
from product.models import Product, Service
from about.models import AboutUs


# home page view
def home(request):
    recent_products = Product.objects.order_by("-created")  # order products from newest to oldest
    services = Service.objects.all()
    aboutus = AboutUs.objects.last()
    return render(request, 'home/index.html',
                  context={"products": recent_products, "services": services, "aboutus": aboutus})
