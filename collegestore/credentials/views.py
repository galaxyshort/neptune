from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('greetings')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
        return redirect('/')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user created")
                return redirect('login')

        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('index')

def greetings(request):
    return render(request, "greetings.html")

def form(request):
    return render(request, "forms.html")





