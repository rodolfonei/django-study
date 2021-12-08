from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse
from form.models import Request

class RequestCreate(CreateView):
    model = Request
    fields = '__all__'
