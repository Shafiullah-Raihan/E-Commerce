from django.shortcuts import render, redirect,HttpResponse
from adminpanel.models import category, product,product_image,customer
from website.models import add_to_cart,checkout

def index(request):
    all_cat = category.objects.all()
    all_product = product.objects.all()
    
    # all_product = product.objects.filter()
    context = {
        'all_cat':all_cat,
        'all_product':all_product,
        
    }
    return render(request,'website/index.html',context)


def about(request):
    return render(request,'website/about.html')


def add_to_carts(request,id):
    if request.session.has_key('customer_session'):
        add_to_cart_list = add_to_cart(
            product_id_id = id,
            customer_id_id = request.session.get('customer_session',id)
        )
        add_to_cart_list.save()
        return redirect('website_home')
    else:
        return redirect('customer_login')
    
def cartList(request):
    if request.session.has_key('customer_session'):
        cart_list_item = add_to_cart.objects.filter(cart_status = 1)
        return render(request,'website/cart_list.html',{'cart_list_item':cart_list_item})
    else:
        return redirect('customer_login')
    

def cart_delete(request,id):
    if request.session.has_key('customer_session'):
       cart_list_item = add_to_cart.objects.filter(id=id)
       cart_list_item.delete()
       return redirect('cartList')
    else:
        return redirect('customer_login')
    
def cart_update(request,id):
    if request.session.has_key('customer_session'):
       if request.method == 'POST':
        qtt = request.POST.get('qtt')
        cart_up = add_to_cart.objects.filter(id=id).update(
            quantity = qtt
        )
        # cart_up = add_to_cart(
        #     id =id,
        #     quantity = qtt
        # )
        # cart_up.save()
       return redirect('cartList')
    else:
        return redirect('customer_login')


def checkout_cart(request):
    if request.session.has_key('customer_session'):
        cart_list = add_to_cart.objects.filter(customer_id = request.session['customer_session'])

        # return HttpResponse(cart_list)
    
        checkout_save = checkout(
            customer_info_id = request.session['customer_session'],            
        )
        checkout_save.save()
        checkout_save.cart_item.set(cart_list)

        for i in  cart_list:
            i.cart_status = False
            i.save()  

        return redirect('website_home')