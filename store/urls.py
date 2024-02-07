from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.item_list, name='home'),
    path('item/<slug:slug>/', views.item_detail, name='item_detail'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('order-summary', views.order_summary, name='order-summary'),
    path('store/', views.store_view, name='online-store'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success')
    ]
