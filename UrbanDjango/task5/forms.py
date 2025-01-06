from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Введите пароль")
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Повторите пароль")
    age = forms.IntegerField(label="Введите свой возраст", min_value=1, max_value=120)
