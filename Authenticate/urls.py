from django.urls import path
from Authenticate import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path('reset/', views.reset, name="reset"),
    # path("logout/", LogoutView.as_view(), name="logout"),
]
