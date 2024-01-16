from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.item_list, name='home' ),
    path('item/<slug:slug>/', views.item_detail, name='item_detail'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),

]