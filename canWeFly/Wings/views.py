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


def get_data_in_time():
    import requests
    from datetime import datetime
    from datetime import timedelta
    from django.core.cache import cache
    url = r'http://10.175.94.58:8088/report_message_four/'
    data = {
        "selectedLeader": "All",
        "selectedTeam": "All",
        "_time": datetime.now().strftime('%Y-%m-%d'),
        "selected_22_dep": "All"
    }

    # conn = get_redis_connection('default')
    result_str = cache.get(data["_time"])

    if result_str and 'F1241138' in result_str:
        pass
        # msg = 'Ops, no shot on the redis data!'
        # return HttpResponse(msg)
    else:
        response = requests.post(url=url, data=data)
        if response.status_code != 200:
            pass
        else:
            result_str = response.content.decode('utf-8')

            # get expires time----until today
            time_delta = datetime.combine(datetime.now().date() + timedelta(days=1),
                                          datetime.strptime("0000", "%H%M").time()) - datetime.now()
            # conn.set('Work', result_str, timeout=time_delta.seconds)
            cache.set(data["_time"], result_str, timeout=time_delta.seconds)


def get_work_time(request):
    import json
    from datetime import datetime
    # from datetime import timedelta
    # import requests
    from django.core.cache import cache

    # employee_id = 'F1241138'
    employee_id = request.GET.get('id')

    if not isinstance(employee_id, str):
        return HttpResponse("Something wrong with the id: " + str(employee_id))

    # url = r'http://10.175.94.58:8088/report_message_four/'
    # data = {
    #     "selectedLeader": "All",
    #     "selectedTeam": "All",
    #     "_time": datetime.now().strftime('%Y-%m-%d'),
    #     "selected_22_dep": "All"
    # }
    time_now = datetime.now().strftime('%Y-%m-%d')
    # conn = get_redis_connection('default')
    # result_str = cache.get('Work')
    result_str = cache.get(time_now)
    if not result_str:
        # 用以解决django.core.cache自动会为key添加版本号，而get不到数据
        # todo:这句话有够蠢得，因为压根就不是这里的代码问题，而是下面的if-else写的有问题
        new_key = cache.make_key(time_now)
        result_str = cache.get(new_key)
    else:
        pass
    # if result_str:
    #     pass
    #     # msg = 'Ops, no shot on the redis data!'
    #     # return HttpResponse(msg)
    # else:
    #     response = requests.post(url=url, data=data)
    #     if response.status_code != 200:
    #         pass
    #     else:
    #         result_str = response.content.decode('utf-8')
    #
    #         # get expires time----until today
    #         time_delta = datetime.combine(datetime.now().date() + timedelta(days=1),
    #                                       datetime.strptime("0000", "%H%M").time()) - datetime.now()
    #         # conn.set('Work', result_str, timeout=time_delta.seconds)
    #         cache.set(data["_time"], result_str, timeout=time_delta.seconds)
    if not result_str:
        return HttpResponse('还没有数据进账，所以查看不了啦。。。')
    else:
        pass
    result_json = json.loads(result_str)
    if isinstance(result_json, list) and result_json:
        total_people_number = len(result_json)
        san_fen_yi = total_people_number - (int(total_people_number / 3) * 2)
        san_fen_er = total_people_number - int(total_people_number / 3)

        avg_over_yi = float(result_json[san_fen_yi]['a_avgoverhours'])
        avg_over_er = float(result_json[san_fen_er]['a_avgoverhours'])

        for i in range(total_people_number):
            if result_json[i]['a_employee'].lower() == employee_id.lower():
                employee_avg_over = float(result_json[i]['a_avgoverhours'])
                total_days = int(result_json[i]['a_totaldays']) + 1
                if employee_avg_over <= avg_over_er:
                    need_avg_over = avg_over_er - employee_avg_over
                    need_over = need_avg_over * total_days
                    msg = str(i) + '/' + str(total_people_number) + ' G2天数：' + str(result_json[i]['a_g2_days']) + \
                          " 已经加班：" + str(result_json[i]['a_totaloverhours']) + '! ' + str(result_json[i]['a_name']) + \
                          '---革命尚未成功，同志们仍需努力： ' + str(need_over) + ' 小时！！'
                    return HttpResponse(msg)
                else:
                    if employee_avg_over <= avg_over_yi:
                        more_avg_over = employee_avg_over - avg_over_er
                        more_over_er = more_avg_over * total_days

                        more_avg_over = avg_over_yi - employee_avg_over
                        more_over_yi = more_avg_over * total_days
                        msg = str(i) + '/' + str(total_people_number) + ' G2天数：' + str(result_json[i]['a_g2_days']) + \
                              ' 已经加班：' + str(result_json[i]['a_totaloverhours']) + '! ' + str(result_json[i]['a_name']) + \
                              '---真是太完美啦，正好卡在中间,真是太努力啦，已经超过了倒数三分之一的： ' + str(more_over_er) + \
                              ' 小时！！\n' + '距离倒数三分之二的时间还差： ' + str(more_over_yi) + ' 小时！！\n'
                        return HttpResponse(msg)
                    else:
                        more_avg_over = employee_avg_over - avg_over_yi
                        more_over_er = more_avg_over * total_days
                        msg = str(i) + '/' + str(total_people_number) + ' G2天数：' + str(result_json[i]['a_g2_days']) + \
                              ' 已经加班：' + str(result_json[i]['a_totaloverhours']) + '! ' + result_json[i]['a_name'] + \
                              '---真是太努力啦，已经超过了倒数三分之二的：' + str(more_over_er) + ' 小时！！\n'
                        return HttpResponse(msg)
        return HttpResponse("Cant fund the id: " + employee_id + " !")
    return HttpResponse("No Data Come in!")


def downloadfile1(request):
    from django.http import Http404
    # file_path = r'F:\bug\20230424_ort35\OTA Keyword.xlsx'
    file_path = r'F:\OTAORT35\OTA Keyword.xlsx'
    # file_path = r'C:\Users\F1241138\.condarc'
    try:
        r = HttpResponse(open(file_path, "rb"))
        print(r)
        r["content_type"] = "application/octet-stream"
        # r["Content-Disposition"] = "attachment;filename=OTA Keyword.xlsx"
        r["Content-Disposition"] = "attachment;filename=OTA Keyword.xlsx"
        return r
    except Exception:
        raise Http404("Download error")


def downloadfile2(request):
    from django.http import StreamingHttpResponse
    from django.http import Http404
    file_path = r"E:\ide-eval-resetter-2.3.5-c80a1d.zip"
    try:
        r = StreamingHttpResponse(open(file_path, "rb"))
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=ide-eval-resetter-2.3.5-c80a1d.zip"
        return r
    except Exception:
        raise Http404("Download error")


def downloadfile3(request):
    from django.http import FileResponse
    from django.http import Http404
    file_path = r"F:\bug\20230610_ort35\Veyron_Cell&WiFi__2023_06_09_NightShift.xlsx"
    try:
        f = open(file_path, "rb")
        r = FileResponse(f, as_attachment=True, filename="Veyron_Cell&WiFi__2023_06_09_NightShift.xlsx")
        return r
    except Exception:
        raise Http404("Download error")


# 上传文件
def uploadfile(request):
    import os
    from django.http import HttpResponse
    from django.shortcuts import render
    from django.conf import settings
    if request.method == 'GET':
        return render(request, "upload.html")
    elif request.method == 'POST':
        myFile = request.FILES.get('myfile', None)
        if myFile:
            # path = os.path.join(settings.MEDIA_ROOT)
            # path = 'E:\\learn_django\\canWeFly\\Wings\\uploads\\'
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)
            dest = open(os.path.join(settings.MEDIA_ROOT, myFile.name), 'wb+')
            # TODO: 注意：为了避免read()方法一次性将文件读取到内存中造成内存不足的问题，使用f.chunks()方式将文件分块处理。
            for chunk in myFile.chunks():
                dest.write(chunk)
            dest.close()
            return HttpResponse('Upload File Success!')
        else:
            return HttpResponse('NO FILE HAS BEEN CHEESED!')
