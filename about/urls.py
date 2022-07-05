from django.urls import path
from . import views

app_name = "about"
urlpatterns = [
    path("", views.about_us, name="about"),  # "about us" panel
    path("contact-us", views.ContactUsView.as_view(), name="contact_us")
]
