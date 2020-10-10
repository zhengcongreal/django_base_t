from django.urls import path

from booktest import views

urlpatterns = [
    path('bookinfo/', views.BookInfoCUIDView.as_view()),
    path('heroinfo/', views.HeroInfoCUIDView.as_view()),

]
