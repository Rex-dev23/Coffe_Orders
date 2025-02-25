from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('update/<int:pk>/', views.order_update, name='order_update'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),
    path('revenue/', views.revenue_report, name='revenue_report'),
    path('api/orders/', views.OrderListAPI.as_view(), name='order_api_list'),
]