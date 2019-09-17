import requests
from django.shortcuts import render

from bs4 import BeautifulSoup
# Create your views here.

def home(request):
    template = 'base.html'
    return render(request,template,{})


def new_search(request):
    search = request.POST.get('search')
    front_end = {
        'search':search,
    }
    template = 'new_search.html'
    return render(request,template,front_end)
