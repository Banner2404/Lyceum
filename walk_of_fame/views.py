from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from walk_of_fame.models import Record

class HomeView(ListView):
    model = Record
    template_name = 'walk_of_fame/home.html'


class CreateRecordView(CreateView):
    model = Record
    fields = ['name', 'year', 'image']
    template_name = 'walk_of_fame/create_record.html'
    success_url = reverse_lazy('home')