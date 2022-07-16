from django.urls import path

from accounts import views

# api/
urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/<str:pk>/', views.user_detail, name='user_detail'),
    
    path('customers/', views.customers, name='customers'),
    path('customers/<str:pk>/', views.customer_detail, name='customer_detail'),
]
