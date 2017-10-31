from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def index(request):
    context = {}
    if request.user.is_authenticated():
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
            st = Client.objects.filter(Username=user)[0]
            login(request, user)
            student = Client.objects.filter(Username=user)
            context = {}
            #context['avatar'] = usrInfo[0].Avatar.url[4:]
            #request.session['studentAvatar'] = student[0].Avatar.url[4:]
            #request.session['user'] = user.username
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
            context={}
            context['message'] = 'ثبت نام شما با موفقیت انجام شد.پس از تایید میتوانید در سیستم وارد شوید'
            return render(request, 'login.html', context)
    else:
        context = {}
        context['message'] = 'لطفا فیلد های فرم را به درستی پر کنید'
        return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')

