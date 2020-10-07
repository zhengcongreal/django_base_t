from django.shortcuts import render
from django import http
# Create your views here.
def register(request):
    return http.HttpResponse('这里假装返回注册页面')