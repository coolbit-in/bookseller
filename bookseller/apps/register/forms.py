# coding:utf-8
from django import forms

class RegisterForm(forms.Form):
    """
    Register Form, parse in register.html
    """
    username = forms.CharField(label='username', max_length=30)

    e_mail = forms.CharField(label='e_mail', max_length=75)

    password = forms.CharField(label='password', max_length=16,
                               widget=forms.PasswordInput)

    errors = {'username': '用户名不正确', 'e_mail': 'e_mail地址不正确', 'password': '密码格式不正确'}



class LoginForm(forms.Form):
    """
    Login Form, parse in login.html
    """

    username = forms.CharField(label='username', max_length=30)

    password = forms.CharField(label='password', max_length=16,
                               widget=forms.PasswordInput)

    errors = {'username': '用户名不正确', 'password': '密码格式不正确'}
