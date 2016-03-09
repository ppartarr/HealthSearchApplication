from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from health_search.settings import STATIC_PATH
from datetime import datetime


def index(request):
    response = render(request, 'eHealth/index.html')
    return response

def about(request):
    return render(request, 'eHealth/about.html')

def search(request):
    return render(request, 'eHealth/search.html')