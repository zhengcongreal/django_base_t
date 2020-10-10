from django import http
from django.shortcuts import render

# Create your views here.

from django.views import View

from booktest.models import HeroInfo, BookInfo


class BookInfoCUIDView(View):
    def get(self, request):
        # print(BookInfo.objects.all())
        book = BookInfo.objects.get(btitle='西游记')
        print(book.id)
        print(book.bcomment)
        print(BookInfo.objects.count())

        return http.HttpResponse("我在这里做bookinfo的cuid!")


class HeroInfoCUIDView(View):
    def get(self, request):
        # HeroInfo.objects.create(hname="白龙马",hgender=0,hbook_id=5)

        # hero=HeroInfo.objects.get(hname="猪悟能")
        # hero.hname="猪八戒"
        # hero.save()

        # 使用模型类.objects.filter().update()，会返回受影响的行数

        HeroInfo.objects.filter(hname="猪八戒").update(hname="天蓬元帅")

        # hero=HeroInfo.objects.get(id=21)
        # hero.delete()

        # 2）模型类.objects.filter().delete()
        # HeroInfo.objects.filter(id=20).delete()

        return http.HttpResponse("我在这里做heroinfo的cuid!")
