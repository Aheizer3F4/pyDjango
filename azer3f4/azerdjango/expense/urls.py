from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               # Home page
    path('list/', views.expense_list, name='expense_list'),  # Expense List page
    path('about/', views.about, name='about'),       # About page
]
