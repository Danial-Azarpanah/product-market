from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# This model is for the about us panel with title, description and etc
class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    instagram = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/about_us", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "aboutus"


# This class is for the members of company's team
class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profession = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="images/team_members", null=True)
    github = models.CharField(max_length=50, null=True)
    instagram = models.CharField(max_length=50, null=True)
    linkedin = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name_plural = "team members"


# This class is for the messages users can send through contact us panel
class Message(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
