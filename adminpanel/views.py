from django.shortcuts import render,redirect
from adminpanel.models import User,category,product,product_image,customer
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import make_password,check_password
import sweetify
from website.models import checkout,add_to_cart


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'admin/index.html')
    else:
        return redirect('login_user')

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:
            return redirect('registration')
        else:
            user_reg = User.objects.create_user(username,email,password_1)
            user_reg.first_name = password_2
            user_reg.save()
            return redirect('login_user')
    return render(request,'admin/user_panel/reg.html')

def login_user(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('psw')
        user_check = authenticate(username = a, password = b)

        if user_check != None:
            login(request,user_check)
            return redirect('dashboard')
        else:
            return redirect('login_user')
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request,'admin/user_panel/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login_user')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            old_pass = request.POST.get('old_pass')
            new_pass = request.POST.get('new_pass')
            confirm_pass = request.POST.get('confirm_pass')

            check_user = User.objects.get(id=request.user.id)
            if check_user.check_password(old_pass) and new_pass == confirm_pass:
                check_user.set_password(new_pass)
                check_user.save()
                update_session_auth_hash(request,check_user)
                return redirect('logout_user')
            else:
                return redirect('change_pass')

        return render(request,'admin/user_panel/change_pass.html')
    else:
        return redirect('login_user')

def user_profile(request):
    if request.user.is_authenticated:
        check_user = User.objects.get(id=request.user.id)
        if request.method == 'POST' and request.FILES:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            image = request.FILES['image']

            user_info = User(
                id = request.user.id,
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                user_image = image,
                password = request.user.password
            )
            user_info.save()
            # user_info = User.objects.update(
            #     first_name = first_name,
            #     last_name = last_name,
            #     email = email,
            #     username = username,
            #     user_image = image
            # )
            
        return render(request,'admin/user_panel/user_profile.html',{'user_info':check_user})
    else:
        return redirect('login_user')

def category_store(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cat_name = request.POST.get('cat_name')
            # cat_pics = request.FILES['image'] if request.FILES else None
            # cat_pics = request.FILES['image']
            if cat_name != "":
                if request.FILES:
                    cat_pics = request.FILES['image']
                else:
                    cat_pics = None

                cat_store = category(
                    cat_name = cat_name,
                    cat_img = cat_pics
                )
                cat_store.save()
                # sweetify.toast(request, 'You successfully Save Category')
                # sweetify.info(request, 'Message sent', button='Ok', timer=3000)
                sweetify.toast(request, 'Oops, something went wrong !', icon="error", timer=30000)
            else:
                return redirect('cat_store')

        return render(request,'admin/Category/cat_store.html')
    else:
        return redirect('login_user')
def cat_show(request):
    if request.user.is_authenticated:
        
        all_category = category.objects.all()

        return render(request,'admin/Category/cat_show.html',{'all_category':all_category})
    else:
        return redirect('login_user')

def create_product(request):
    if request.user.is_authenticated:     
        cat = category.objects.all()
        if request.method == 'POST':
            cat_name = request.POST.get('category_id')
            product_name = request.POST.get('product_name')
            product_old_price = request.POST.get('product_old_price')
            product_new_price = request.POST.get('product_new_price')
            description = request.POST.get('description')
            product_pic = request.FILES.getlist('product_pic') if request.FILES else None

            product_store = product(
                product_name = product_name,
                cat_id = cat_name,
                product_old_price = product_old_price,
                product_new_price = product_new_price,
                product_description = description
            )
            product_store.save()
            product_id = product_store.id

            if product_pic != None:
                for i in product_pic:
                    prod_img = product_image(
                        product_image = i,
                        product_id_id = product_id
                    )
                    prod_img.save()


        return render(request,'admin/product/Add_product.html',{'cat':cat})
    else:
        return redirect('login_user')
    
def product_show(request):
    if request.user.is_authenticated:
        
        product_all = product.objects.all()

        return render(request,'admin/product/product_show.html',{'product_all':product_all})
    else:
        return redirect('login_user')
    
def Customer_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pass_1 = request.POST.get('pass_1')
        pass_2 = request.POST.get('pass_2')

        if pass_1 == pass_2:
            customer_reg = customer(
                username = username,
                email = email,
                mobile = mobile,
                password = make_password(pass_1)
            )
            customer_reg.save()
            return redirect('customer_login')

    return render(request,'admin/customer/signup.html')

def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass_1')
        
        user_cahek = customer.customer_check(username)
        if user_cahek:
            password_check = check_password(password,user_cahek.password)
            if password_check:
                request.session['customer_session'] = user_cahek.id
                return redirect('website_home')
        else:
            return redirect('customer_login')  
    return render(request,'admin/customer/login.html')

# def customer_admin(request):
#     if request.session.has_key('customer_session'):
#         return render(request,'admin/customer/customer_dashboard.html')
#     else:
#         return redirect('customer_login') 
    
def customer_logout(request):
    try:
        del request.session['customer_session']
        return redirect('website_home')
    except:
        pass
    return redirect('customer_login') 


def cart_history(request):
    if request.user.is_authenticated:
        
        cart_his = checkout.objects.all()

        return render(request,'admin/cart_history/cat_history.html',{'cart_his':cart_his})
    else:
        return redirect('login_user')