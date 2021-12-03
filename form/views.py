from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RequestForm

def create(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Form submission successful')

    return render(request, 'create.html', {'form': form})