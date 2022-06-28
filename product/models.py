from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    price = models.FloatField()
    description = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    image = models.ImageField(upload_to="images/products", null=True)
