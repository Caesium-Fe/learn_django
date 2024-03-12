# from django.conf.urls import url
from django.urls import path, re_path
# from . import views
from Wings import views
from Wings.Timer import Timer


urlpatterns = [
    # 当用户访问bookapp应用的主页时, 执行视图函数index,反向根据名称获取url地址;
    path(r'', views.index, name='index'),
    re_path(r'asd/', views.login, name='asd'),
    path(r'chaxun/', views.chaxun_td, name='chaxun'),
    path(r'xiugai/', views.xiugai_td, name='xiugai'),
    path(r'shanchu/', views.shanchu_td, name='shanchu'),
    path(r'jiaban/', views.get_work_time, name='jiaban'),
    path(r'xiazai1/', views.downloadfile1, name='xiazai1'),
    path(r'xiazai2/', views.downloadfile2, name='xiazai2'),
    path(r'xiazai3/', views.downloadfile3, name='xiazai3'),
    # path(r'biaodan/', views.biaodan, name='biaodan_1'),
    path(r'shangchuan/', views.uploadfile, name='uploadfile'),
]

Timer().start()
Timer.add_every_minutes_job(60, views.get_data_in_time)
