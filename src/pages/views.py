from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings

# Create your views here.
@login_required
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

@login_required
def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

@login_required
def resume_view(request, *args, **kwargs):
    return render(request, "resume.html", {})

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGIN_URL, '/'))