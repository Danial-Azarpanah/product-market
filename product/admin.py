from django.contrib import admin

from .models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('product',)
    search_fields = ('body', 'product__title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    search_fields = ('title', 'id', 'slug')
    list_display = ('title', 'price', 'show_image')


admin.site.register(Category)
admin.site.register(Service)
