from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    games = {
        "Atomic Heart": "Купить",
        "Cyberpunk 2077": "Купить",
        "PayDay 2": "Купить"
    }

    return render(request, 'third_task/shop.html', {'games': games})


def cart(request):
    cart_items = ["Atomic Heart - 1 шт.", "Cyberpunk 2077 - 2 шт.", "PayDay 2 - 1 шт."]
    total_price = "5000 рублей"
    return render(request, 'third_task/cart.html', {'cart_items': cart_items, 'total_price': total_price})
