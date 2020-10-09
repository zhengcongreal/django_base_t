from django.shortcuts import render
from django.views import View
from django import http
import json


# Create your views here.
# 、分别利用查询字符串、表单、json字符串传参的方式，
# 由postman向后端传递姓名、年龄、邮箱三个参数并在控制台上打印。
class QSParamterView(View):
    def get(self, request):
        name = request.GET.get('name')
        age = request.GET.get('age')
        email = request.GET.get('email')
        print("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))
        return http.HttpResponse("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))


class FormDataParamterView(View):
    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        print("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))
        return http.HttpResponse("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))


class JsonParamterView(View):
    def post(self, request):
        json_str = request.body
        mydict = json.loads(json_str)
        name = mydict.get('name')
        age = mydict.get('age')
        email = mydict.get('email')
        print("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))
        return http.HttpResponse("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))


class UrlParamterView(View):
    def get(self, request, name, age, email):
        print("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))
        return http.HttpResponse("姓名：%s 年龄：%s 邮箱: %s" % (name, age, email))
