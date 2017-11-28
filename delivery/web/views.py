from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *

# Create your views here.

def index(request):
    context = {}
    if request.user.is_authenticated():
        context['products'] = Product.objects.all()
        return render(request, 'index.html', context)
    else :
        return login_view(request)


@csrf_exempt
def login_view(request):
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name="Seller").user_set.all()
            if user in users_in_group :
                login(request, user)
                context = {}
                context['categories'] = Category.objects.all()
                return render(request, 'panel.html', context)
            else:
                login(request, user)
                st = Client.objects.filter(Username=user)[0]
                student = Client.objects.filter(Username=user)
                context = {}
                #context['avatar'] = usrInfo[0].Avatar.url[4:]
                #request.session['studentAvatar'] = student[0].Avatar.url[4:]
                request.session['user'] = user.username
                context['products'] = Product.objects.all()
                return render(request, 'index.html', context)
        else:
            context = {}
            context['message'] ='نام کاربری یا پسورد وارد شده اشتباه میباشد'
            return render(request, 'login.html', context)
    else:
        context = {}
        return render(request, 'login.html', context)



def register(request):
    if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        if User.objects.filter(email=request.POST['email']).exists() or User.objects.filter(username=request.POST['username']).exists():
            context = {}
            context['message']='مشخصات وارد شده تکراری میباشد'
            return render(request, 'register.html', context)
        else:
            username = request.POST['username']
            password = request.POST['password']
            #phone = request.POST['phone']
            email = request.POST['email']
            name = request.POST['name']
            family = request.POST['family']
            user = User.objects.create_user(username, email, password)
            user.save()
            student = Client(Username=user, Name=name, Family=family)
            student.save()
            basket = Basket(Owner=user)
            basket.save()
            context={}
            context['message'] = 'ثبت نام شما با موفقیت انجام شد.پس از تایید میتوانید در سیستم وارد شوید'
            return render(request, 'login.html', context)
    else:
        context = {}
        context['message'] = 'لطفا فیلد های فرم را به درستی پر کنید'
        return render(request, 'register.html', context)

def registerSeller(request):
    if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        if User.objects.filter(email=request.POST['email']).exists() or User.objects.filter(username=request.POST['username']).exists():
            context = {}
            context['message']='مشخصات وارد شده تکراری میباشد'
            return render(request, 'registerSeller.html', context)
        else:

            group = Group.objects.get(name='Seller')
            username = request.POST['username']
            password = request.POST['password']
            #phone = request.POST['phone']
            email = request.POST['email']
            name = request.POST['name']
            #family = request.POST['family']
            user = User.objects.create_user(username, email, password)
            user.groups.add(group)
            user.save()
            student = Client(Username=user, Name=name)
            student.save()
            context={}
            context['message'] = 'ثبت نام شما با موفقیت انجام شد.پس از تایید میتوانید در سیستم وارد شوید'
            return render(request, 'login.html', context)
    else:
        context = {}
        context['message'] = 'لطفا فیلد های فرم را به درستی پر کنید'
        return render(request, 'registerSeller.html', context)


def addproduct(request):
    context = {}
    if 'productname' in request.POST and 'category' in request.POST and 'price' in request.POST and 'stock' in request.POST :
        productname = request.POST['productname']
        cat = request.POST['category']
        price = request.POST['price']
        stock = request.POST['stock']
        category = Category.objects.filter(Name=cat)[0]
        newproduct = Product(Name=productname, Price=price, Category=category, Stock=stock)
        newproduct.save()
        context['message']='محصول جدید با موفقیت اضافه شد'
    else :
        context['message'] = 'مشخصات را به درستی وارد کنید'
    context['categories'] = Category.objects.all()
    return render(request, 'panel.html', context)


def search(request):
    context = {}
    req = request.POST.get('srchterm', False)
    result = Product.objects.filter(Name__contains=req)
    if not result:
        context['notFind'] = True
    context['products'] = result
    return render(request, 'index.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')


def addtobasket(request , productid):
    context = {}
    basket = Basket.objects.filter(Owner=request.user)[0]
    list = basket.ProductList.all()
    mark = 0
    for p in list :
        if int(p.Product.id) == int(productid) :
            p.Quantity = p.Quantity+1
            p.save()
            mark = 1
    if mark == 0 :
        newProduct = ProductOfBasket(Quantity=1, Product=Product.objects.get(id=productid))
        newProduct.save()
        basket.ProductList.add(newProduct)
        basket.save()


    context['products'] = Product.objects.all()
    return render(request, 'index.html', context)

def showbasket(request):
    context = {}
    basket = Basket.objects.filter(Owner=request.user)[0]
    list = basket.ProductList.all()
    context['basket'] = list
    return  render(request , 'showbasket.html' , context)