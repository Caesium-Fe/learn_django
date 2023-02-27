# from django.conf.urls import url
from django.urls import path, re_path
# from . import views
from Wings import views


urlpatterns = [
    # 当用户访问bookapp应用的主页时, 执行视图函数index,反向根据名称获取url地址;
    path(r'', views.index, name='index'),
    re_path(r'asd/', views.login, name='asd'),
    path(r'chaxun/', views.chaxun_td, name='chaxun'),
    path(r'xiugai/', views.xiugai_td, name='xiugai'),
    path(r'shanchu/', views.shanchu_td, name='shanchu'),
    path(r'biaodan/', views.biaodan, name='biaodan_1'),
]

