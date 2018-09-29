from django.urls import path 
from . import views

urlpatterns = [
    path('', views.criar_chamado, name='criar_chamado'),
]
