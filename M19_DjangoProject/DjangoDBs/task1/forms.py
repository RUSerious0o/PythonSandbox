from django.forms import Form, CharField, PasswordInput, NumberInput


class SignUpForm(Form):
    username = CharField(max_length=30, label='Введите логин')
    password = CharField(widget=PasswordInput, min_length=8, label='Введите пароль')
    repeat_password = CharField(widget=PasswordInput, min_length=8, label='Повторите пароль')
    age = CharField(widget=NumberInput, max_length=3, label='Введите свой возраст')
