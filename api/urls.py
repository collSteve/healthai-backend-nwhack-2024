from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.health_instruction, name='health_instruction')
]
