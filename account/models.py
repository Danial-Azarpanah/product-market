from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


class Profile(models.Model):
    """
    Profiles of users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/profile', null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html(f'<h3 style="color: red">No image</h3>')

    show_image.short_description = 'image'
