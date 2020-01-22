from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('V2H1', views.V2H1, name='V2H1'),
]
