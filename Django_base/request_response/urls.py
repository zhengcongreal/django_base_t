from  django.urls import path,re_path
from . import views
urlpatterns = [
    # 测试提取查询字符串参数：http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/',views.QSParamterView.as_view()),
    path('formdataparamter/',views.FormDataParamterView.as_view()),
    path('json/',views.JasonParamterView.as_view()),
    path('urlparamter/<int:age>',views.URLParam1View.as_view()),
    path('urlparamter2/<mobilephone:phone_num>',views.URLParam2View.as_view()),
    re_path(r'^urlparamter3/(?P<phone_num>1[3-9]\d{9})/$',views.URLParam3View.as_view()),
    path('headparamter/',views.HeadersParamView.as_view()),
    path('jsonresponse/',views.JsonResponseView.as_view()),
    path('index/', views.IndexView.as_view(), name='index'),
    path('redirect_index/', views.LoginRedictView.as_view())

]
