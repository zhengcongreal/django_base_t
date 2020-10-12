from django import http
from django.db.models import F, Q, Sum, Max, Min, Avg
from django.shortcuts import render


# Create your views here.

from django.views import View

from booktest.models import HeroInfo, BookInfo


class BookInfoCUIDView(View):
    def get(self, request):
        # print(BookInfo.objects.all())
        # book = BookInfo.objects.get(btitle='西游记')
        # print(book.id)
        # print(book.bcomment)
        # print(BookInfo.objects.count())

        # BookInfo.objects.create(btitle="金瓶梅",bpub_date='1800-1-1',bread=10000,bcomment=200000)
        # BookInfo.objects.filter(btitle="金瓶梅").update(btitle="三国志")
        # BookInfo.objects.create(btitle="聊斋",bpub_date="1890-5-23",bread=1000,bcomment=556)
        # BookInfo.objects.filter(btitle="聊斋").delete()

        # 1）相等

        # exact：表示判等。

        # 例：查询编号为1的图书。
        # book=BookInfo.objects.filter(id__exact=1)
        # print(book)

        # 2）模糊查询
        #
        # contains：是否包含。

        # book = BookInfo.objects.filter(btitle__contains="志")
        # print(book)

        # startswith、endswith：以指定值开头或结尾。

        # 例：查询书名以
        '部'
        # 结尾的图书

        # 3） 空查询
        # isnull：是否为null。
        # # 例：查询书名不为空的图书。
        #
        #
        # book=BookInfo.objects.filter(btitle__isnull=False)
        # print(book)

        # 4） 范围查询
        #
        # in ：是否包含在范围内。
        #
        # 例：查询编号为1或3或5的图书

        # book=BookInfo.objects.filter(id__in=[1,3,5])
        # print(book)

        # 5）比较查询
        #
        # gt
        # 大于(greater
        # then)
        # gte
        # 大于等于(greater
        # then
        # equal)
        # lt
        # 小于(less
        # then)
        # lte
        # 小于等于(less
        # then
        # equal)
        # 例：查询编号大于3的图书
        # book=BookInfo.objects.filter(id__gt=3)
        # print(book)
        # 不等于的运算符，使用exclude()
        # 过滤器。
        #
        # 例：查询编号不等于3的图书
        # book=BookInfo.objects.exclude(id=3)
        # print(book)

        # 6）日期查询

        # year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算。
        # book=BookInfo.objects.filter(bpub_date__gte="1990-1-1")
        # print(book)

        # F对象
        # 之前的查询都是对象的属性与常量值比较，两个属性怎么比较呢？ 答：使用F对象，被定义在django.db.models中。

        # 语法如下：
        # 例：查询阅读量大于等于评论量的图书。
        # book=BookInfo.objects.filter(bread__gte=F('bcomment'))
        #
        # print(book)
        # 例：查询阅读量大于2倍评论量的图书。

        # book=BookInfo.objects.filter(bread__gt=F('bcomment')*2)

        # Q对象
        # 多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字。

        # 例：查询阅读量大于20，并且编号小于3的图书。
        # book=BookInfo.objects.filter(bread__gt=20,id__lt=3)
        # book=BookInfo.objects.filter(Q(bread__gt=20)&Q(id__lt=3))
        # book=BookInfo.objects.filter(Q(bread__gt=20)&Q(pk__lt=3))
        # Q对象可以使用 &、 | 连接， & 表示逻辑与， | 表示逻辑或。
        # 例：查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
        # book=BookInfo.objects.filter(Q(bread__gt=20)|Q(pk__lt=3))
        # Q对象前可以使用
        # ~操作符，表示非not。
        # 例：查询编号不等于3的图书。
        # book=BookInfo.objects.filter(~Q(pk=3))
        # book=BookInfo.objects.exclude(pk=3)
        #
        # 聚合函数
        # 使用aggregate()
        # 过滤器调用聚合函数。聚合函数包括：Avg
        # 平均，Count
        # 数量，Max
        # 最大，Min
        # 最小，Sum
        # 求和，被定义在django.db.models中。
        #
        # 例：查询图书的总阅读量。

        # book=BookInfo.objects.aggregate(Sum('bread'))
        # book2=BookInfo.objects.aggregate(Max('bread'))
        # book3=BookInfo.objects.aggregate(Min('bread'))
        # book4=BookInfo.objects.aggregate(Avg('bread'))
        # result=book.get("bread__sum")
        # book1=BookInfo.objects.filter(pk__gt=0).count()
        #
        # print(BookInfo.objects.all().order_by('bread'))
        # print(BookInfo.objects.all().order_by('-bread'))

        return http.HttpResponse()


class HeroInfoCUIDView(View):
    def get(self, request):
        # hero=HeroInfo(hname="如来佛祖",hgender=0,hbook_id=5)
        # hero.save()
        # HeroInfo.objects.create(hname="白龙马",hgender=0,hbook_id=5)
        # hero=HeroInfo.objects.get(hname="猪悟能")
        # hero.hname="猪八戒"
        # hero.save()
        # 使用模型类.objects.filter().update()，会返回受影响的行数
        # HeroInfo.objects.filter(hname="猪八戒").update(hname="天蓬元帅")
        # hero=HeroInfo.objects.get(id=21)
        # hero.delete()
        # 2）模型类.objects.filter().delete()
        # HeroInfo.objects.filter(id=20).delete()

        # 5.4
        # 关联查询
        # 由一到多的访问语法：

        # 一对应的模型类对象.多对应的模型类名小写_set

        # b=BookInfo.objects.get(pk=1)
        # b1=BookInfo.objects.get(pk=2)
        # b2=BookInfo.objects.get(pk=3)
        # print(b.heroinfo_set.all())
        # print(b1.heroinfo_set.all())
        # print(b2.heroinfo_set.all())
        #

        # 由多到一的访问语法:
        # 多对应的模型类对象.多对应的模型类中的关系类属性名
        # 例
        # print(HeroInfo.objects.get(pk=1).hbook)

        # 关联过滤查询
        # 查询图书，要求图书英雄为
        # "孙悟空"
        # book= BookInfo.objects.filter(heroinfo__hname="孙悟空")

        # 查询图书，要求图书中英雄的描述包含
        "八"
        # book1=BookInfo.objects.filter(heroinfo__hname__contains="天")

        # 查询书名为“天龙八部”的所有英雄。
        # hero=HeroInfo.objects.filter(hbook__btitle="天龙八部")
        # 查询图书阅读量大于30的所有英雄
        # hero=HeroInfo.objects.filter(hbook__bread__gt=30)
        # 对查询集可以再次调用过滤器进行过滤，如
        book = BookInfo.objects.filter(bread__gt=30).order_by('bpub_date')
        qs = BookInfo.objects.all()
        print([i.id for i in qs])
        print([i.id for i in qs])
        print([i.id for i in qs])
        print([i.id for i in qs])
        return http.HttpResponse(book)
