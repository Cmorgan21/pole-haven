from django.urls import path
from . import views

urlpatters = [
    path('', views.PostList.as_view(), name="blog-page" )


]