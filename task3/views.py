from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Platform',
        'heading': 'Главная страница',
        'link1': 'Главная',
        'link2': 'Магазин',
        'link3': 'Корзина',
    }
    return render(request, 'third_task/index.html', context)


def store(request):
    context = {
        'title': 'Store',
        'heading': 'Книги автора: Ден Браун',
        'list1': 'Ангелы и демоны',
        'list2': 'Код Да Винчи',
        'list3': 'Утраченный символ',
        'list4': 'Инферно',
        'button': 'КУПИТЬ',
    }
    return render(request, 'third_task/store.html', context)


def cart(request):
    context = {
        'title': 'Cart',
        'heading': 'Корзина',
        'content': 'Корзина пока что пуста. Чтобы добавить товары '
                   'нажмите кнопку КУПИТЬ в магазине'
    }
    return render(request, 'third_task/cart.html', context)
