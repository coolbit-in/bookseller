from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext

def show_404_view(request):
    render_to_response('404.html')