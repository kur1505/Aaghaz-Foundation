from django.urls import path
from Website import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index', views.index, name="index"),   
]
