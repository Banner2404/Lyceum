from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from walk_of_fame.models import Record

class HomeView(ListView):
    model = Record
    template_name = 'walk_of_fame/home.html'

    def get_queryset(self):
        qs = Record.objects.order_by('year')
        result = dict()
        for record in qs:
            if result.get(record.year) is None:
                result[record.year] = []
            result[record.year].append(record)
        return sorted(result.items(), key=lambda x: x[0], reverse=True)


class CreateRecordView(CreateView):
    model = Record
    fields = ['name', 'description', 'profile', 'year', 'image']
    template_name = 'walk_of_fame/create_record.html'
    success_url = reverse_lazy('home')