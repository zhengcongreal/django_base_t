from . import views
from django.urls import path
urlpatterns = [
                path('qsp_info/',views.QSParamterView.as_view()),
                path('form_data/',views.FormDataParamterView.as_view()),
                path('json_data/',views.JsonParamterView.as_view()),
                path('url_paramter/<str:name>/<int:age>/<email:email>',views.UrlParamterView.as_view()),
]
