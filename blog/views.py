from django.shortcuts import render, get_object_or_404
from.models import Post
from django.views import generic


# Create your views here.

class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1)
    template_name = "blog/blog_page.html"
    paginate_by = 6

def blog_details(request, slug):
    query = Post.objects.filter(status=1)
    post= get_object_or_404(query, slug=slug)

    return render(
        request,
        "blog/blog_detail.html",
        {"post":post}
    )
