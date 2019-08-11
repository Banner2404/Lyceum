from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from walk_of_fame.models import Record

def home(request):
    return render(request, 'walk_of_fame/home.html')

class CreateRecord(CreateView):
    model = Record
    fields = ['name']
    template_name = 'walk_of_fame/create_record.html'
    success_url = reverse_lazy('home')