from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views import generic
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse





# Create your views here.

class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1)
    template_name = "blog/blog_page.html"
    paginate_by = 6

def blog_details(request, slug):
    query = Post.objects.filter(status=1)
    post= get_object_or_404(query, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()

    return render(
        request,
        "blog/blog_detail.html",
        {"post":post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,}
        )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('blog_details', args=[slug]))

