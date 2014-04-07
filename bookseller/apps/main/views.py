from django.http import HttpResponse
from django.http import Http404
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
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from bookseller.apps.main import models, forms

def index(request):
    return HttpResponse("hello")

@login_required(login_url='/account/login')
def create(request):
    if request.method == 'POST':
        form = forms.ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            info_dict = form.cleaned_data
            info_dict['published_time'] = now()
            info_dict['lasted_update_time'] = info_dict['published_time']
            info_dict['status'] = 1
            info_dict['left_number'] = info_dict['number']

            # get the tag type.
            tag_id=info_dict['tags']
            tag = models.Tags.objects.get(pk=tag_id)
            del info_dict['tags']
            info_dict['tag'] = tag

            # get the owner of the created object.Add the relationship.
            user = User.objects.get(username=request.user.username)
            info_dict['owner'] = user

            new_item = models.Item(**info_dict)
            new_item.save()


          #  user.item_set.add(new_item)

            return HttpResponseRedirect(reverse('item_detail', args=(new_item.id,)))
        else:
            print "valid failed!"
            return HttpResponseRedirect('/item/create')
    else:
        form = forms.ItemCreateForm()
        tag_list = models.Tags.objects.all()
    return render_to_response('item_create.html', {'form' : form, 'tag_list': tag_list}, context_instance=RequestContext(request))

@login_required(login_url='/account/login')
def detail(request, pk):
    item = models.Item.objects.get(id=pk)
    # TODO: handle order form.
    if request.method == 'POST':
        form = forms.ItemOrderForm(request.POST)
        if form.is_valid():
            if item.left_number > 0:
                # get the owner of the created object.Add the relationship.
                user = User.objects.get(username=request.user.username)
                item.queue.add(user)
                item.save()
                # TODO:add message.
    return render_to_response('item_detail.html', {'item' : item}, context_instance=RequestContext(request))

@login_required(login_url='/account/login')
def update(request, pk):
    # TODO: handle item delete and image delete.
    item = try_get_item_by_id(pk)
    user = get_user(request)

    # check if it is the creator.
    if user.username != item.owner.username:
        raise Http404
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
            return HttpResponseRedirect(reverse('item_detail', args=(item.id)))
        else:
            # TODO: handle failed post.
            return HttpResponseRedirect('/fail')
    else:
        return render_to_response('item_update.html', {'item' : item, 'user': user}, context_instance=RequestContext(request))


@login_required(login_url='/account/login')
def delete(request, pk):
    item = try_get_item_by_id(pk)
    user = get_user(request)

    # check if it is the creator.
    if user.username == item.owner.username:
        item.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/fail/')


def get_user(request):
    user = User.objects.get(username=request.user.username)
    return user

def try_get_item_by_id(id):
    try:
        item= models.Item.objects.get(id=id)
    except:
        raise Http404
    return item
