from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
import re
from datetime import datetime
from walk_of_fame.forms import LogMessageForm
from walk_of_fame.models import LogMessage

# Create your views here.

def hello(request, name):
    return render(
        request, 
        'walk_of_fame/hello_there.html', 
        {
            'name': name,
            'date': datetime.now()
        })

class HomeListView(ListView):
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, 'walk_of_fame/about.html')

def contact(request):
    return render(request, 'walk_of_fame/contact.html')

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, 'walk_of_fame/log_message.html', {'form': form})
