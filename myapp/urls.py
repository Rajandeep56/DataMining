from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('upload', views.upload_csv, name='upload'),
    path('success', views.upload_success, name='upload_success'),
    path('displaydata', views.display_data, name='display_data'),

   # path('register', views.register, name="register"),
]
