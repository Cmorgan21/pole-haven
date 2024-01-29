from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.site_header = "Pole Haven Admin"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'author__username')
    list_filter = ('status', 'created_on')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')

