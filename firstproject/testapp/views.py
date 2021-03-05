from django.shortcuts import render
from django.http import HttpResponse
def helloview(request):
    s='<h1 style="color:red;">hello welcome to first django project from pycharm</h1>'
    return HttpResponse(s)

