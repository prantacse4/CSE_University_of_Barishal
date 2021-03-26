from django.shortcuts import render

# Create your views here.

def homepage(request):
    diction = {}
    return render(request, 'csebu/public_home.html', context=diction)


def wrong_urls(request):
    diction = {}
    return render(request, 'csebu/wrong_urls.html', context=diction)