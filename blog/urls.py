from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="blog-page" ),
    path('<slug:slug>/', views.blog_details, name="blog_details"),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]