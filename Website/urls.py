from django.urls import path
from Website import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.index, name="index"),  
    # <--------------------------------- Donor Urls ---------------------------------------------------> 
    path('donor_list/', views.donor_list, name="donor_list"),
    path('donor_create/', views.donor_create, name="donor_create"),

    # <--------------------------------- Volunteer Urls --------------------------------------------------->
    path('volunteers_list/', views.volunteers_list, name="volunteers_list"),
    path('volunteer_create/', views.volunteer_create, name="volunteer_create"),

    # <--------------------------------- Beneficiary Urls --------------------------------------------------->
    path('beneficiarys_list/', views.beneficiarys_list, name="beneficiarys_list"),
    path('beneficiary_create/', views.beneficiary_create, name="beneficiary_create"),
]
