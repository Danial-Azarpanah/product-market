from django.shortcuts import render
from .models import AboutUs, TeamMember
from django.views.generic import CreateView
from .models import Message
from django.urls import reverse_lazy
from .mixins import LoginAuthenticateMixin


# about_us panel
def about_us(request):
    aboutus = AboutUs.objects.last()
    members = TeamMember.objects.all()
    return render(request, "about/about.html", {"aboutus": aboutus, "team_members": members})


class ContactUsView(LoginAuthenticateMixin, CreateView):
    model = Message
    fields = ("subject", "text")
    success_url = reverse_lazy("main:home")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
