from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, authenticate, logout
from .registerform import RegisterForm

# Create your views here.


def home(request):
    product_list = Product.objects.all()
    return render(request, "home.html",{'products': product_list})

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pswd')

        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {'error':'Please, Check Your Credentials to Login, some error in it..'})
        
    else:
     return render(request, "login.html", {})

def louout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('home')
            
    form = RegisterForm()
    return render(request, "register.html" ,{'form': form} )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
        
    return render(request, "register.html", {'form': form})


def product(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, "product.html", {'product':product})