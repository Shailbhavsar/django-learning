from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request,"home.html",{"title":"My Home",'products' : products})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request,"contact.html")

def view_product(request,pk):
    data = get_object_or_404(Product,pk=pk)
    return render(request,"view_product.html",{'data' : data})

@login_required
def add_student(request):
    if request.method == "POST":
        stu_name = request.POST.get("stu_name", "").strip()
        stu_email = request.POST.get("stu_email", "").strip()

        if not stu_name or not stu_email:
            return render(request, "add-student.html", {"err_msg": "Please fill the form"})
        isExists = Student.objects.filter(email=stu_email)
        if isExists:
            return render(request, "add-student.html", {"err_msg": "Email already exists"})

        Student.objects.create(name=stu_name, email=stu_email)
        return redirect("home")

    return render(request, "add-student.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request,user)
            return redirect("home")
        else:
            return render(request, "login.html", {"err_msg": "Invalid username or password"})
    return render(request, "login.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not username or not email or not password:
            return render(request, "signup.html", {"err_msg": "Please fill all fields."})
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"err_msg": "That username is already taken."})

        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"err_msg": "That email is already registered."})

        User.objects.create_user(username=username, email=email, password=password)
        return redirect("login")

    return render(request, "signup.html")


def logout(request):
    auth_logout(request)
    return redirect('login')