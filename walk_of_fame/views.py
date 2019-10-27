from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from walk_of_fame.models import Record
from django.core.mail import mail_admins
from django.conf import settings
from threading import Thread

class HomeView(ListView):
    model = Record
    template_name = 'walk_of_fame/home.html'

    def get_queryset(self):
        qs = Record.objects.filter(active=True).order_by('year')
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
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        response = super(CreateRecordView, self).form_valid(form)
        message = render_to_string('walk_of_fame/email.html', {'object': self.object})
        #EmailThread(message).start()
        return response

def success_view(request):
    return render(request, 'walk_of_fame/success.html')

class EmailThread(Thread):

    def __init__(self, message):
        self.message = message
        Thread.__init__(self)

    def run(self):
        mail_admins("Новая запись", "", html_message=self.message)
