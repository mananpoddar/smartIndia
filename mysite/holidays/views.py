from django.shortcuts import render, redirect
from .models import HolidayImage
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def new_image(request):
    if request.method == 'POST':
        form = forms.HolidayImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('holidays:process')
    else:
        form = forms.HolidayImageForm
    return render(request, 'holidays/image_enter.html', {'form':form})

def image_process(request):
    images = HolidayImage.objects.all()
    return render(request, 'holidays/process_image.html', {'images':images})