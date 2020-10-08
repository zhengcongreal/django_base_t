
from django.urls import path,re_path
from . import views
urlpatterns = [
    # path('users/register/',views.register),
    re_path(r'^users/register/$',views.RegisterView.as_view()),
    path('users/testmixin/',views.TestMiXinView.as_view()),
    re_path(r'^users/loginview/$',views.LoginView.as_view()),
    # url(r'^users/login/$',views.LoginView.as_view()),


]
