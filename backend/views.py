#coding: utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

__author__ = 'lidong'
@csrf_exempt
def index(request):
    #client_ip = request.COOKIES['csrftoken']
    return render(request,'index.html')