from django import http
from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare1(MiddlewareMixin):
    """自定义中间件"""

    def process_request(self, request):
        print("process_request被调用前")
        # return http.HttpResponseNotAllowed(["get","post"])

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("process_view1被调用！")

    def process_response(self, request, response):
        print("process_response1被调用！")
        return response


class TestMiddleWare2(MiddlewareMixin):
    """自定义中间件"""

    def process_request(self, request):
        print("process_request2被调用！")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("process_view2被调用！")

    def process_response(self, request, response):
        print("process_response2被调用！")
        return response
