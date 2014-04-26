# coding:utf-8
from __future__ import unicode_literals
import time
from django.http import HttpResponse
from django.http import HttpRequest

from django.http import HttpResponseRedirect
from django.db.models import Q
from django.template import Context
from django.template.loader import get_template

from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, RequestContext
from django.http import Http404

from forms import RegisterForm, LoginForm
from bookseller.apps.main.models import UserInfo, Item, Tags, Messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
def list(request, tag_name, page_num):
    if tag_name != '全部':
        try:
            tag = Tags.objects.get(name=tag_name)
        except Tags.DoesNotExist:
            raise Http404

        item_list = Item.objects.filter(tag=tag).order_by('-published_time')
        items_count_num = Item.objects.filter(tag=tag).order_by('-published_time').count()
    else:
        item_list = Item.objects.order_by('-published_time')
        items_count_num = Item.objects.order_by('-published_time').count()

    page_num = int(page_num)
    list_length = 2
    posts = {}
    item_list = item_list[list_length * (page_num - 1):list_length * page_num]
    posts['page_number'] = page_num
    posts['pages_count_number'] = -(-items_count_num / list_length)
    posts['previous_page_number'] = page_num - 1
    posts['next_page_number'] = page_num + 1
    if page_num > posts['pages_count_number']:
        raise Http404
    if page_num > 1:
        posts['has_previous'] = True
    if page_num < posts['pages_count_number']:
        posts['has_next'] = True
    tag_list = Tags.objects.all().order_by('id')

    return render_to_response('list.html', {'item_list': item_list, 'posts': posts, 'tag_list': tag_list},
                              context_instance=RequestContext(request))


def show_search(request):
    return render_to_response('search.html', context_instance=RequestContext(request))


def register(request):
    """
    This function is used to process registration requests
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print "form is valid"
            info_dict = form.cleaned_data
            new_user = User.objects.create_user(username=info_dict['username'],
                                                email=info_dict['e_mail'],
                                                password=info_dict['password'])
            new_user.is_active = True
            #new_user.date_joined = time.asctime()
            new_user.save()
            new_user_info = UserInfo(user_id=new_user,
                                     phone_number=int(info_dict['phone_number']),
                                     qq_number=int(info_dict['qq_number']),
                                     address=info_dict['address'])
            new_user_info.save()
            user = auth.authenticate(username=info_dict['username'], password=info_dict['password'])
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            print "form is not valid"
            return HttpResponseRedirect('/account/register/')
    else:
        form = RegisterForm()
    return render_to_response('register.html', {'school_list': ['西安电子科技大学']}, context_instance=RequestContext(request))


#def my_login(request):
#    if request.method == 'POST':
#        return login(request=request, template_name='login.html', )
#
#def my_logout(request):
#    return logout(request=request, template_name='logout.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 使用  username 和 password 的认证登录系统
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            #print user

            # 注册完成后直接登录
            if user != None:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/account/errors/invalid_login/')
        else:
            return HttpResponseRedirect("/account/errors/invalid_login/")
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


def logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        auth.logout(request)
        return HttpResponseRedirect('/')


@login_required(login_url='/account/login/')
def account(request, id):
    user_id = int(id)
    #if user_id == User.objects.get(username=user.username).id:
    #    return render_to_response('account.html', {})
    #else:
    try:
        account_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404
    account_user_info = UserInfo.objects.get(user_id=user_id)
    render_dict = {}
    render_dict['name'] = account_user.username
    render_dict['email'] = account_user.email
    render_dict['phone_number'] = account_user_info.phone_number
    render_dict['qq_number'] = account_user_info.qq_number
    render_dict['address'] = account_user_info.address
    #print render_dict
    item_list = Item.objects.filter(owner=account_user).order_by('-published_time')

    return render_to_response('person.html', {'user_info': render_dict, 'item_list': item_list},
                              context_instance=RequestContext(request))


@login_required(login_url='/account/login/')
def messages(request):
    user = User.objects.get(username=request.user.username)

    # about django.db.models.Q(), to see:
    # https://docs.djangoproject.com/en/1.5/topics/db/queries/
    # If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.
    # 选择 form_id 或者 to_id 是 当前用户的 Messages
    message_list = Messages.objects.filter(Q(from_id=user) | Q(to_id=user))

    print message_list
    return render_to_response('messages.html', {'message_list': message_list}, context_instance=RequestContext(request))


def error_login_invalid(request):
    return render_to_response('errors/invalid_login.html', {}, context_instance=RequestContext(request))