from django.shortcuts import render


# Create your views here.
def get_main_page(request):
    return render(request, 'third_task/main.html', context={})


def get_shop_page(request):
    return render(request, 'third_task/shop.html', context={
        'goods_list': [
            'Atomic Heart',
            'Cyberpunk',
            'PayDay 2'
        ]
    })


def get_cart_page(request):
    return render(request, 'third_task/cart.html', context={
        'cart_is_empty': True
    })
