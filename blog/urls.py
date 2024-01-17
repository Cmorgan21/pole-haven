from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="blog-page" ),
    path('<slug:slug>/', views.blog_details, name="blog_details")


]