from django.shortcuts import render
from django import http
from django.views import View
# # Create your views here.
# # def register(request):
# #     # print("request:%s"%request)
# #     if request.method=="GET":
# #
# #         return http.HttpResponse('这里假装返回注册页面')
# #     elif request.method=="POST":
# #         return http.HttpResponse('这里假装实现注册逻辑')


# 7. 类视图添加扩展类
class ListModelMiXin(object):
    def list(self,request,*args,**kwargs):
        print("这是一个mixin扩展类！")
        return http.HttpResponse('这是一个MiXin扩展类！')

class CreateModelMiXin(object):
    def create(self,request,*args,**kwargs):
        print("这是一个mixin扩展类2！")
        pass


class TestMiXinView(ListModelMiXin,CreateModelMiXin,View):
    def get(self,request):
        return  self.list(request)

    def post(self,request):

       return self.create(request)

class RegisterView(ListModelMiXin,CreateModelMiXin,View):
    def get(self,request):
        self.create(request)
        return http.HttpResponse('这里假装返回注册页面')

    def post(self, request):
        return http.HttpResponse('这里假装实现注册逻辑')


class LoginView(View):
    def get(self,request):
        return http.HttpResponse("假装这是一个登录页面！")

    def post(self, request):
        return http.HttpResponse('假装实现登录逻辑')


class SayView(View):
    """测试路由屏蔽
    http://127.0.0.1:8000/say/
    """

    def get(self, request):
        return http.HttpResponse('say')


class SayHelloView(View):
    """测试路由屏蔽
    http://127.0.0.1:8000/sayhello/
    """

    def get(self, request):
        return http.HttpResponse('say hello')