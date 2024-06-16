from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def view_func(request):
    if request.method == 'GET':
        return HttpResponse('Got request')
    elif request.method == 'POST':
        return HttpResponse('POST request')
