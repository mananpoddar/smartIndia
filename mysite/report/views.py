from django.shortcuts import render, redirect
from .models import Report,Images
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from . import forms
from django.forms import formset_factory, modelformset_factory

# Create your views here.
def report(request):
    ImageFormSet = modelformset_factory(Images, form=forms.ImageForm, extra=3)
    if request.method == 'POST':
        reportForm = forms.ReportForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if reportForm.is_valid() and formset.is_valid():
            report_form = reportForm.save(commit=False)
            report_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(report=report_form, image=image)
                photo.save()
            messages.success(request,
                             "Posted!")
            return HttpResponseRedirect("/")
        else:
            print(reportForm.errors, formset.errors)
    else:
        reportForm = forms.ReportForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'reportfraud.html',
                  {'reportForm': reportForm, 'formset': formset})
