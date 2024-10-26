from django.http import HttpRequest
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Author, Post


posts_per_page = 2


# Create your views here.
def get_main_page(request: HttpRequest):
    global posts_per_page

    posts = Post.objects.all().order_by('-creation_date')
    if request.method == 'POST':
        posts_per_page = request.POST.get('posts_per_page')
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main.html', context={
        'page_obj': page_obj,
    })
