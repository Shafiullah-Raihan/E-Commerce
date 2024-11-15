from website.models import add_to_cart


def context_processor(request):
    cart_count = add_to_cart.objects.filter(cart_status = 1).count()

    context = {
        'cart_count':cart_count
    }
    return context