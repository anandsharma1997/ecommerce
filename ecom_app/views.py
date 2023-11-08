from django.shortcuts import render, redirect
from .models import Product , Category
from django.contrib.auth import login, authenticate, logout
from .registerform import RegisterForm
from django.contrib import messages

# Create your views here.

# Showing all the product in home page
def home(request):
    product_list = Product.objects.all()
    return render(request, "home.html",{'products': product_list})

# This is for About us page 
def about(request):
    return render(request, "about.html", {})

# Login page
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
    

# Logout button function
def louout_user(request):
    logout(request)
    return redirect('home')

# User Registration page

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

# Single product page
def product(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, "product.html", {'product':product})


# Category page for products
def categoryPage(request, gname):
    category = Category.objects.get(name=gname)
    products = Product.objects.filter(category=category)
    print(category)
    print(products)
    return render(request, "categoryPage.html", {'category': category, 'products': products})


# 404 page
def custom_404(request, invalid_path):
    return render(request, '404.html', {'invalid_path': invalid_path}, status=404)


# cart page

def cart_summary(request):
    return render(request, "cart_summary.html", {})