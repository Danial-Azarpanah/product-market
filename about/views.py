from django.shortcuts import render
from .models import AboutUs, TeamMember


# about_us panel
def about_us(request):
    aboutus = AboutUs.objects.last()
    members = TeamMember.objects.all()
    return render(request, "about/about.html", {"aboutus": aboutus, "team_members": members})
