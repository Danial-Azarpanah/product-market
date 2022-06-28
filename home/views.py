from django.shortcuts import render
from about.models import AboutUs
from product.models import Service, Category, Product


# home page view
def home(request):
    aboutus = AboutUs.objects.last()
    services = Service.objects.all()
    products = Product.objects.all()

    return render(request, 'home/index.html',
                  context={"aboutus": aboutus, "services": services, "products": products})
