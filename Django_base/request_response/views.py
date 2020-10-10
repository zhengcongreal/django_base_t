from django.shortcuts import render, redirect, reverse
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


# 3. URL路径参数：提取URL路径中的特定部分数据

class URLParam1View(View):
    """测试path()提取普通路径参数
       http://127.0.0.1:8000/url_param1/18/
       """
    def get(self,request,age):
        return  http.HttpResponse('年龄：%d'%age)
    # def get(self,request,path):
    #     return  http.HttpResponse('年龄：%s'%path)

class URLParam2View(View):
    """测试path()中自定义路由转换器提取路径参数：手机号
    http://127.0.0.1:8000/url_param2/18500001111/
    """
    def get(self,request,phone_num):
        return  http.HttpResponse('手机号：%s'%phone_num)

class URLParam3View(View):
    """测试path()中自定义路由转换器提取路径参数：手机号
    http://127.0.0.1:8000/url_param3/18500001111/
    """
    def get(self,request,phone_num):
        return  http.HttpResponse('手机号：%s'%phone_num)


class HeadersParamView(View):
    """测试提取请求头参数"""

    def get(self, request):
        # 获取请求头中文件的类型
        ret = request.META.get('CONTENT_LENGTH')
        return http.HttpResponse(ret)


class JsonResponseView(View):
    def get(self,request):

        dict_data={
            'city':'wuhan',
            'subject':'python'
        }
        # 将python字典自动转成json数据，相当于json.dumps
        return http.JsonResponse(dict_data)


# 3. redirect()：重定向

class IndexView(View):
    """测试重定向
    http://127.0.0.1:8000/index/
    """

    def get(self, request):
        print("正在处理视图")
        return http.HttpResponse('假装这是个网站首页')


class LoginRedictView(View):
    def get(self, request):
        ret_url = reverse('request_response:index')
        return redirect(ret_url)


class ImageResponseView(View):
    def get(self, request):
        with open(r"D:\Program Files\code\django_base_t\Django_base\request_response\img\2.jpeg", 'rb') as file:
            file_data = file.read()

        return http.HttpResponse(file_data, content_type="image/jpeg")
