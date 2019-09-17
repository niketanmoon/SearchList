import requests
from requests.compat import quote_plus
from django.shortcuts import render

from bs4 import BeautifulSoup


from .models import Search

CRAIGSLIST_URL = 'https://indore.craigslist.org/search/?query={}'
# Create your views here.

def home(request):
    template = 'base.html'
    return render(request,template,{})


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search = search)
    # formatting the url
    url = CRAIGSLIST_URL.format(quote_plus(search))
    # getting the response from the site through requests
    response = requests.get(url)
    # storing it in text format in a data variable
    data = response.text
    # Creating an object of soup that will contain all the html
    # it is parsing the html data
    soup = BeautifulSoup(data,features = 'html.parser')

    #for finsing through id and tags and classes
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'
        final_postings.append((post_title, post_url, post_price))


    front_end = {
        'search':search,
        'final_postings':final_postings,
    }
    template = 'new_search.html'
    return render(request,template,front_end)
