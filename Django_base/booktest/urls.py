from django.urls import path

from booktest import views

urlpatterns = [
    path('bookinfo/', views.BookInfoCUIDView.as_view()),
    path('heroinfo/', views.HeroInfoCUIDView.as_view()),
    path('bookview/', views.BookView.as_view()),
    path('setcookie/', views.SetCookie.as_view()),
    path('getcookie/', views.GetCookie.as_view()),
    path('setsession/', views.SetSession.as_view()),
    path('getsession/', views.GetSession.as_view()),

]
