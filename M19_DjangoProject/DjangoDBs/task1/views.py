from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpResponse

from .forms import SignUpForm
from .models import Buyer, Game


# Create your views here.
def get_main_page(request):
    return render(request, 'task1/main.html', context={})


def get_shop_page(request):
    return render(request, 'task1/shop.html', context={
        'games': Game.objects.all()
    })


def get_cart_page(request):
    return render(request, 'task1/cart.html', context={
        'cart_is_empty': True
    })


def get_info(username, pwd, repeat_pwd, age):
    info = {
            'username': username,
            'age': age,
            'error': []
        }

    if Buyer.objects.filter(name=username).exists():
        info['error'].append('Пользователь уже существует')

    if pwd != repeat_pwd:
        info['error'].append('Пароли не совпадают')

    if int(age) < 18:
        info['error'].append('Вы должны быть старше 18')

    return info


def sign_up_by_django(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(f'username: {form.cleaned_data["username"]}\n'
                  f'password: {form.cleaned_data["password"]}\n'
                  f'repeat_password: {form.cleaned_data["repeat_password"]}\n'
                  f'age: {form.cleaned_data["age"]}')

        info = get_info(
            form.cleaned_data['username'],
            form.cleaned_data['password'],
            form.cleaned_data['repeat_password'],
            form.cleaned_data['age']
        )

        if len(info['error']) == 0:
            Buyer.objects.create(name=info['username'], age=info['age'], balance=0)
            return HttpResponse(f"Приветствуем, {info['username']}!")
        else:
            info['form'] = form
            return render(request, 'task1/registration_page.html', context=info)
    else:
        form = SignUpForm()
    return render(request, 'task1/registration_page.html', context={'form': form})