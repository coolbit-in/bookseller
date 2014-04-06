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
from django.contrib.auth.decorators import permission_required

from bookseller.apps.main import models, forms
from bookseller.apps.register.views import user_auth_test

def index(request):
    return HttpResponse("hello")

@permission_required(user_auth_test, login_url='/account/login')
def create(request):
    if request.method == 'POST':
        form = forms.ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            info_dict = form.cleaned_data
            info_dict['published_time'] = now()
            info_dict['status'] = 1
            new_item = models.Item(**info_dict)
            new_item.save()
            return HttpResponseRedirect('/success')
        else:
            print "valid failed!"
            return HttpResponseRedirect('/item/create')
    else:
        form = forms.ItemCreateForm()
    return render_to_response('item_create.html', {'form' : form}, context_instance=RequestContext(request))

@permission_required(user_auth_test, login_url='/account/login')
def detail(request, pk):
    item = models.Item.objects.get(id=pk)
    return render_to_response('item_detail.html', {'item' : item}, context_instance=RequestContext(request))

@permission_required(user_auth_test, login_url='/account/login')
def update(request, pk):
    item = models.Item.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.ItemUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            info_dict = form.cleaned_data
            item.description = info_dict['description']
            item.price = info_dict['price']
            # TODO: delete the original image
            if info_dict['image']:
                item.image = request.FILES['image']
            item.number = info_dict['number']
            item.save()
            return HttpResponseRedirect('/success')
        else:
            return HttpResponseRedirect('/fail')
    else:
        return render_to_response('item_update.html', {'item' : item}, context_instance=RequestContext(request))


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

