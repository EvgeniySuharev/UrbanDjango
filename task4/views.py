from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Platform'
    }
    return render(request, 'fourth_task/index.html', context)


def store(request):
    context = {
        'title': 'Store',
        'list': ['Ангелы и демоны', 'Код Да Винчи',
                 'Утраченный символ', 'Инферно'],
        'button': 'КУПИТЬ'
    }
    return render(request, 'fourth_task/store.html', context)


def cart(request):
    context = {
        'title': 'Cart',
        'content': 'Корзина пока что пуста. Чтобы добавить товары '
                   'нажмите кнопку КУПИТЬ в магазине'
    }
    return render(request, 'fourth_task/cart.html', context)
