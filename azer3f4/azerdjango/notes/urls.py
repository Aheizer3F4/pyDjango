from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.note_list, name='note_list'),
    path('about/', views.about, name='about'),
]
