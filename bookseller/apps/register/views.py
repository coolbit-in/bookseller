# coding:utf-8
import time
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect

from django.template import Context
from django.template.loader import get_template

from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, RequestContext

from forms import RegisterForm, LoginForm
from bookseller.apps.main.models import UserInfo

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
                                                password=info_dict['password'],)
            new_user.is_active = True
            #new_user.date_joined = time.asctime()
            new_user.save()
            return HttpResponseRedirect('/')
        else:
            print "form is not valid"
            return HttpResponseRedirect('register/')
    else:
        form = RegisterForm()
    return render_to_response('register.html', {}, context_instance=RequestContext(request))


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
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print user
            if user != None:
                 auth.login(request, user)
                 return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/errors/invalid_login/')
        else:
            return HttpResponseRedirect("/errors/invalid_login/")
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form' : form}, context_instance=RequestContext(request))

def account(request, id):
    user_id = int(id)
    request_user = request.user
    if request_user.is_authenticated():
        #if user_id == User.objects.get(username=user.username).id:
        #    return render_to_response('account.html', {})
        #else:
        account_user = User.objects.get(id=user_id)
        account_user_info = UserInfo.objects.get(user_id=user_id)

        render_dict = {}
        render_dict['name'] = account_user.username
        render_dict['email'] = account_user.email
        render_dict['phone_number'] = account_user_info.phone_number
        render_dict['qq_number'] = account_user_info.qq_number
        render_dict['address'] = account_user_info.address

        return render_to_response('person.html', {'user_info ':render_dict})
    else:
        return render_to_response('login.html', {});


def error_login_invalid(request):
    return render_to_response('errors/invalid_login.html',{})