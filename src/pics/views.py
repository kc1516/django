from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from .models import Picture
from .forms import PictureForm

@login_required
def pic_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = PictureForm()
            return redirect("pics")
    else:
        form = PictureForm()

    image = Picture.objects.filter(file_type='image', owner__in=[request.user, 'general'])
    thumbnail = Picture.objects.filter(file_type='thumbnail')
    return render(request, 'pic.html', {'img': image, 'thumb': thumbnail, 'form': form})

def success(request):
    return HttpResponse('successfully uploaded')