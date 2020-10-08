from django.shortcuts import render
from django.views import View
from django import  http
import json
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
# 2.1 表单类型请求体数据(Form Data)

class FormDataParamterView(View):
    def post(self,request):
        name=request.POST.get('name')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        height=request.POST.get('height')
        return http.HttpResponse('接收到表单请求体数据：%s--%s--%s--%s' % (name, age,sex, height))

# 非表单类型请求体数据(Non-Form Data)：JSON
class JasonParamterView(View):
    def post(self,request):
        json_str=request.body
        json_dict_list=json.loads(json_str)
        print(json_dict_list)
        for i in json_dict_list:
            name=i.get('name')
            age=i.get('age')
            print(name,age)
        # name=json_dict.get('name')
        # age=json_dict.get('age')
        # return http.HttpResponse('接收到非表单请求体数据:%s--%d'%(name,age))
        return  http.HttpResponse("假装有数据！")