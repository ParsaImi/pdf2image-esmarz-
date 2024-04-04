from django.shortcuts import render
from django.http import HttpResponse
from .utils import start

collection = start()
# mycollection = collection['roads']['posts']



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Dbconnecting(request):
    print(collection)
    return HttpResponse(f"{collection}Hello, world. You're at the polls index.")
    