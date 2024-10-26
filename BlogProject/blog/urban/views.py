from django.shortcuts import render

from .models import Author, Post


# Create your views here.
def get_main_page(request):
    return render(request, 'main.html', context={
        'posts': Post.objects.all(),
    })
