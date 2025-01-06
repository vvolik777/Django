from django.shortcuts import render
from .forms import UserRegister

users = ['admin', 'user1', 'testuser']  # псевдо-список пользователей


def sign_up_by_html(request):  # рега через HTML
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            info['success'] = username  # передаём имя пользователя для приветствия

    return render(request, 'fifth_task/registration_page.html', {'info': info})


def sign_up_by_django(request):  # рега через джанго форму
    info = {}
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                info['success'] = username

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', {'info': info})
