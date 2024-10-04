from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm


def get_info(username, pwd, repeat_pwd, age):
    users = [
        'Mike',
        'Pete',
        'Jake',
        'Ann',
    ]

    info = {
            'username': username,
            'age': age,
            'error': []
        }

    if username in users:
        info['error'].append('Пользователь уже существует')

    if pwd != repeat_pwd:
        info['error'].append('Пароли не совпадают')

    if int(age) < 18:
        info['error'].append('Вы должны быть старше 18')

    return info

# Create your views here.
def sign_up_by_html(request):
    if request.method == 'POST':
        print(f'username: {request.POST.get("username")}\n'
              f'password: {request.POST.get("password")}\n'
              f'repeat_password: {request.POST.get("repeat_password")}\n'
              f'age: {request.POST.get("age")}')

        info = get_info(
            request.POST.get('username'),
            request.POST.get("password"),
            request.POST.get("repeat_password"),
            request.POST.get("age")
        )

        if len(info['error']) == 0:
            return HttpResponse(f"Приветствуем, {info['username']}!")
        else:
            return render(request, 'fifth_task/registration_page.html', context=info)

    return render(request, 'fifth_task/registration_page.html', context={})


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
            return HttpResponse(f"Приветствуем, {info['username']}!")
        else:
            info['form'] = form
            return render(request, 'fifth_task/registration_page.html', context=info)
    else:
        form = SignUpForm()
    return render(request, 'fifth_task/registration_page.html', context={'form': form})
