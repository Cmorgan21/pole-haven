from django.shortcuts import render
from.models import Post
from django.views import generic


# Create your views here.

class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1)
    template_name = "blog/blog_page.html"
    paginate_by = 6
