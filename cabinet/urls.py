from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('new-order/', views.new_order, name='new_order'),
    path('profile/', views.profile, name='profile'),
    path('support/', views.support, name='support'),
    path('api/tilda/lead/', views.tilda_webhook, name='tilda_webhook'),
]
