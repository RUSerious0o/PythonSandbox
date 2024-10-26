from django.contrib import admin

from .models import Author, Post

# Register your models here.
admin.site.register(Author)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title']
    fields = [('id', 'creation_date'), ('title', 'author'), 'content']
