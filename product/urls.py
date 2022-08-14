from django.urls import path

from . import views

app_name = "product"
urlpatterns = [
    path("list", views.ProductListView.as_view(), name="list"),
    path("detail/<slug:slug>", views.product_detail, name="detail"),
]