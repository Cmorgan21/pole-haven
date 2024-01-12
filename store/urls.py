from django.urls import path
from . import views

urlpatterns = [
    path('',views.item_list, name='home' ),
    path('item/<int:item_id>/', views.item_detail, name='item_detail')
]