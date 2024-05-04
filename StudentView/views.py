from django.shortcuts import render
from FacultyView.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from FacultyView.utils import unique_id

# Create your views here.
User = get_user_model()  # Get the User model configured in settings

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, log in the user
            login(request, user)
            return redirect("add_manually")  # Redirect to attendance page or any other page
        else:
            # User is not authenticated, check if user needs to be registered
            if not User.objects.filter(username=username).exists():
                # User does not exist, register the user
                user = User.objects.create_user(username=username, password=password)
                login(request, user)  # Log in the newly registered user
                return redirect("add_manually")  # Redirect to attendance page or any other page
            else:
                # User exists but password is incorrect
                messages.error(request, 'Invalid password')

    
    return render(request, 'StudentView/Login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("add_manually")  # Redirect after successful registration
    else:
        form = UserCreationForm()
    
    return render(request, 'StudentView/register.html', {'form': form})

present = set()


def add_manually_post(request):
    student_roll = request.POST["student-name"]
    student = Student.objects.get(s_roll=student_roll)
    present.add(student)
    return HttpResponseRedirect("/submitted")


def submitted(request):
    return render(request, "StudentView/Submitted.html")
