from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.template import Context
from django.template.loader import get_template
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from bookseller.apps.main import models, forms
def index(request):
    return HttpResponse("hello")

def create(request):
    if request.method == 'POST':
        form = forms.ItemCreateForm(request.POST)
        if form.is_valid():
            info_dict = form.cleaned_data
            info_dict['published_time'] = now()
            info_dict['status'] = 1
            new_item = models.Item(**info_dict)
            new_item.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('register/')
    else:
        form = forms.ItemCreateForm()
    return render_to_response('item_create.html', {'form' : form})


class ItemCreate(CreateView):
    template_name_suffix = '_create'
    model = models.Item
    fields = ['title', 'description', 'price',
                  'number', 'tag', 'status']

class ItemUpdate(UpdateView):
    template_name_suffix = '_update'
    model = models.Item
    fields = ['title', 'description', 'price',
                  'number', 'tag', 'status']
class ItemList(ListView):
    models = models.Item

    def get_context_data(self, **kwargs):
        context = super(ItemList, self).get_context_data(**kwargs)
        return context



