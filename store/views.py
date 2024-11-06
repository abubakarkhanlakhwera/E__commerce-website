from django.shortcuts import render, redirect
from .models import Product , Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm



def category(req, foo):
    # replace hyphen with space
    foo = foo.replace('-','')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(req,'store/category.html',{'products':products,'category':category})
    except:
         messages.success(req, "That Category Doesn't exits")
         return redirect('home')
    

def product(req,pk):
    products = Product.objects.get(id=pk)
       
        
    return render(req, 'store/product.html', {'products': products})
    

def home(req):
    products = Product.objects.all()
    return render(req, 'store/home.html', {'products': products})

def aboutme(req):
    return render(req, 'store/aboutme.html')

def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, "You Have Been Logged In")
            return redirect('home')
        else:
            messages.error(req, "There was an error, Please Login again")
            return redirect('login')
    else:
        return render(req, 'store/login.html')

def logout_user(req):
    logout(req)
    messages.success(req, "You have been logged out...")
    return redirect('home')

def register_user(req):
    form = SignUpForm()
    if req.method == "POST":
        form = SignUpForm(req.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            # Log in the user
            login(req, user)
            messages.success(req, "You have registered successfully!")
            return redirect('home')
        else:
            messages.error(req, "Whoops! There was an error, please register again")
            return redirect('register')
    else:
        return render(req, 'store/register.html', {'form': form})
