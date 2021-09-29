from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='index'),
    path('contact/', views.contact, name='index'),
    path('sale/', views.sale, name='index'),
]