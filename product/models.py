from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.html import format_html
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


# model for the services, company provides
class Service(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/services")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, unique=True)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    image = models.ImageField(upload_to="images/products", null=True)

    def __str__(self):
        return self.title

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Product, self).save()

    def get_absolute_url(self):
        return reverse("product:detail", args=[self.slug])

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="70px" height="40px">')
        return format_html(f'<h3 style="color: red">No image</h3>')

    show_image.short_description = 'image'


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="replies", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.body[:30]}"
