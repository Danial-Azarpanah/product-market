from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html


class AboutUs(models.Model):
    """
    About us panel information
    """
    title = models.CharField(max_length=50)
    body = models.TextField()
    instagram = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/about_us", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "aboutus"


class TeamMember(models.Model):
    """
    Members of the market
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profession = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="images/team_members", null=True)
    github = models.CharField(max_length=50, null=True)
    instagram = models.CharField(max_length=50, null=True)
    linkedin = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "team members"

    def __str__(self):
        return self.user.get_full_name()

    def show_image(self):
        """
        Return object image or "No image" text
        """
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="40px" height="40px">')
        return format_html(f'<h3 style="color: red">No image</h3>')

    show_image.short_description = 'image'


class Message(models.Model):
    """
    User Messages received from Contact us panel
    """
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
