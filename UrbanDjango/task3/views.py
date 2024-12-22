from django.shortcuts import render

def main_page(request):
    return render(request, 'third_task/main_page.html')

def shop_page(request):
    items = {
        'Игровая клавиатура': '1500 руб.',
        'Игровая мышь': '1200 руб.',
        'Игровая гарнитура': '3000 руб.',
    }
    return render(request, 'third_task/shop_page.html', {'items': items})

def cart_page(request):
    return render(request, 'third_task/cart_page.html')