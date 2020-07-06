from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'ca2020app/index.html')


def training_domain(request, domain_id):
    return HttpResponse('You are in this domain: ', domain_id)


def candidate(request, domain_id):
    return HttpResponse('You are %s' % domain_id)


def login(request):
    return render(request, 'ca2020app/login.html')
