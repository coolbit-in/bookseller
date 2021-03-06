# coding:utf-8
from django.http import HttpResponse
from django.db.models import Q
from django.http import Http404, HttpResponseBadRequest
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
from bookseller.apps.main.models import Item, Messages
from bookseller.apps.register.forms import MessageForm


def show_index(request):
    item_list = Item.objects.order_by('-published_time')[0:10]
    return render_to_response('index.html', {'item_list': item_list}, context_instance=RequestContext(request))

def search(request):
    return HttpResponseBadRequest()

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
    tag_list = models.Tags.objects.all()
    item = models.Item.objects.get(id=pk)
    # TODO: handle order form.
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form_dict = form.cleaned_data
            if item.status > 0 and request.user.username == User.objects.get(id=form_dict['from_id']).username:
                message_dict = {}
                message_dict['from_id'] = User.objects.get(id=form_dict['from_id'])
                message_dict['to_id'] = User.objects.get(id=form_dict['to_id'])
                message_dict['item_id'] = models.Item.objects.get(id=form_dict['item_id'])
                message_dict['content'] = form_dict['content']
                message_dict['published_time'] = now()
                new_message = models.Messages(**message_dict)
                new_message.save()

    user = User.objects.get(username=request.user.username)

    # about django.db.models.Q(), to see:
    # https://docs.djangoproject.com/en/1.5/topics/db/queries/
    # If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.
    # 选择 form_id 或者 to_id 是 当前用户的 Messages
    message_list = Messages.objects.filter((Q(from_id=user) | Q(to_id=user)) & Q(item_id=item))

    return render_to_response('item_detail.html', {'item' : item, 'tag_list': tag_list, 'message_list': message_list}, context_instance=RequestContext(request))

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
            return HttpResponseBadRequest()
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
        return HttpResponseBadRequest()


def get_user(request):
    user = User.objects.get(username=request.user.username)
    return user

def try_get_item_by_id(id):
    try:
        item= models.Item.objects.get(id=id)
    except:
        raise Http404
    return item

# TODO: search