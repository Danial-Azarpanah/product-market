from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .models import AboutUs, TeamMember
from .models import Message
from .mixins import LoginAuthenticateMixin


class AboutUsView(TemplateView):
    """
    About us panel with company and staff info
    """
    template_name = 'about/about.html'
    extra_context = {'members': TeamMember.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutus'] = AboutUs.objects.last()
        return context


class ContactUsView(LoginAuthenticateMixin, CreateView):
    """
    Contact us panel
    """
    model = Message
    fields = ("subject", "text")
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        """
        Auto email field completion for logged-in users
        """
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
