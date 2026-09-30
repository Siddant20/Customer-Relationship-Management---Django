
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:cust_id>/', views.customer, name="customer"),
    path('create_order/<str:cust_id>', views.createOrder, name="createOrder"),
    path('update_order/<str:order_id>', views.updateOrder, name="updateOrder"),
    path('delete_order/<str:order_id>', views.deleteOrder, name="deleteOrder"),


]


