from django.urls import path

from . import views

urlpatterns = [
    path('', views.expense_list, name='expense'),
    path('user/', views.userexpense, name='user_expense'),
    path('transaction/', views.create_expense)
]