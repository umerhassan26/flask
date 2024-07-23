from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('web home page')

def shop(request):
    return HttpResponse('web shop page')

def product_details(request,id):
    return HttpResponse(f'web product detals page - id: {id}')
