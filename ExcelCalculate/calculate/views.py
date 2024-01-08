from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate(requset):
    return HttpResponse('calculate, calculate function')
