from django.shortcuts import render
from django.views import View
from django import  http
# 1. 提取查询字符串数据
# Create your views here.
class QSParamterView(View):
    """测试提取查询字符串参数
        http://127.0.0.1:8000/querystring/?name=zxc&age=18
        """
    def get(self,request):
        name=request.GET.get("name")
        age=request.GET.get("age")
        return http.HttpResponse('查询字符串参数：%s--%s' % (name, age))
    # 提取查询字符串参数不区分请求方式，即使客户端进行POST方式的请求，依然可以通过request.GET获取请求中的查询字符串参数。
    def post(self, request):
        name = request.GET.get("name")
        age = request.GET.get("age")
        height = request.GET.get("height",'180')
        return http.HttpResponse('查询字符串参数：%s--%s--%s' % (name, age,height))

class FormDataParamterView(View):

    def post(self,request):
        name=request.POST.get('name')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        height=request.POST.get('height')
        return http.HttpResponse('查询字符串参数：%s--%s--%s--%s' % (name, age,sex, height))