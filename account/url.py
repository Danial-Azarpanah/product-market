from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.login_user, name='login'),  # the url for login panel
    path('register', views.register_user, name='register'),  # the url for register panel
    path('logout', views.logout_user, name='logout')  # the url for logout function
]