from django.contrib import admin

from .models import Author, Post, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['creation_date', 'id', 'author', 'title']
    fields = [('id', 'creation_date'), ('title', 'author'), 'content']
