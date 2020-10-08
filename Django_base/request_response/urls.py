from  django.urls import path
from . import views
urlpatterns = [
    # 测试提取查询字符串参数：http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/',views.QSParamterView.as_view()),
    path('formdataparamter/',views.FormDataParamterView.as_view()),
    path('json/',views.JasonParamterView.as_view()),

]
