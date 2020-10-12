"""Django_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# 在总路由中，注册自定义路由转换器
from converters import MobilePhoneConverter,EmailConverter
from django.urls import register_converter
register_converter(MobilePhoneConverter,"mobilephone")
register_converter(EmailConverter,"email")
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include(('request_response.urls', 'request_response'), namespace='request_response')),
    path('', include('request_response_test.urls')),
    path('', include('booktest.urls')),
]
