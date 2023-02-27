from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django_redis import get_redis_connection


def index(request):
    return HttpResponse("alkjdslkjaskld")


def login(request):
    print('asd')
    conn = get_redis_connection('default')
    conn.set('xx3', 'oo3')
    return HttpResponse('ok')


def chaxun_td(request):
    from Wings.models import Article
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Article.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Article.objects.filter(id=1)

    # 获取单个对象
    response3 = Article.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    var = Article.objects.order_by('title')[0:2]

    # 数据排序
    Article.objects.order_by("id")

    # 上面的方法可以连锁使用
    Article.objects.filter(title="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.title + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def xiugai_td(request):
    from Wings.models import Article

    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Article.objects.get(id=1)
    test1.title = 'Google'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(title='Google')

    # 修改所有的列
    # Test.objects.all().update(title='Google')

    return HttpResponse("<p>修改成功</p>")


def shanchu_td(request):
    from Wings.models import Article

    # 删除id=1的数据
    test1 = Article.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")


def tianjia_book(request):
    from Wings import models
    # 通过实例化对象的save方法存储到数据库
    book = models.Book(title="嘎啦嘎啦", price=300, publish="呼啦出版社", pub_date="2022-09-06")
    book.save()
    # 通过orm提供的objects方法create来实现
    books = models.Book.objects.create(title="阿里嘎多", price=200, publish="呼啦出版社", pub_date="2023-01-01")
    print(books, type(books))
    return HttpResponse("<p>ok</p>")

