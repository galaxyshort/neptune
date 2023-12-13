from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .form import PersonCreationForm
from .models import Person, Course


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

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Please fill the details carefully!")
    return render(request, 'forms.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'forms.html', {'form': form})


def message(request):
    return render(request, 'message.html')


# AJAX
def load_course(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'course': course})
    # return JsonResponse(list(course.values('id', 'name')), safe=False)
