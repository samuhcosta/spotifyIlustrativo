from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('premium', views.premium),
    path('ajuda', views.ajuda),
    path('baixar', views.baixar),
]