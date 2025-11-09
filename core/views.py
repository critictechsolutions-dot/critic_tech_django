from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Account created. You are now able to log in.")
            return redirect("index")
        else:
            messages.error(request, f"{form.errors}")
            print("Form errors:", form.errors)
    else:
        form = SignUpForm()

    context = {
        "form": form,
    }
    return render(request, 'registration/signup.html', context)

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'registration/login.html')

def logout(request):
    django_logout(  request)
    return redirect("index")


def terms_and_conditions(request):
    return render(request,"terms and conditions.html")

def privacy_policy(request):
    return render(request,"privacy.html")






