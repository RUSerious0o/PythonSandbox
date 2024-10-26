from django.shortcuts import render
# from django.core.paginator import Paginator

from .models import Author, Post


# Create your views here.
def get_main_page(request):
    return render(request, 'main.html', context={
        'posts': Post.objects.all().order_by('-creation_date'),
    })
