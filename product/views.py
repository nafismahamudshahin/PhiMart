from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view_products(request):
    return HttpResponse("hello im working")