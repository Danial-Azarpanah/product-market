from django.views.generic import TemplateView

from about.models import AboutUs
from product.models import Service, Category, Product


class HomeView(TemplateView):
    """
    Home page view
    """
    template_name = 'home/index.html'
    extra_context = {'services': Service.objects.all(),
                     'products': Product.objects.all()}

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['aboutus'] = AboutUs.objects.last()
        return context
