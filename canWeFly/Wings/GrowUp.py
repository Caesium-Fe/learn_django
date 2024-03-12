from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
# from django.http import HttpResponse
# from Wings import views


class MiddleWare(MiddlewareMixin):

    # def __init__(self):
    #     super().__init__()

    def process_request(self, request):
        print(r"Grow up process_request method success!", id(request))

    def process_response(self, request, response):
        print(r"Grow up process_response method success!", id(request))
        return response

    def process_view(self, reuqest, view_func, view_args, view_kwargs):
        print(r"md1  process_view 方法！")  # 在视图之前执行 顺序执行
        # return view_func(reuqest)

    def process_exception(self, request, exception):  # 引发错误 才会触发这个方法
        print(r"md1  process_exception 方法！")
        # return HttpResponse(exception) #返回错误信息


class IpMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print("Grow1 up process_request method success!", id(request))

    def process_response(self, request, response):
        print("Grow1 up process_response method success!", id(request))
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        Pass_IPs = ['10.197.24.123', '10.197.24.246', '10.197.24.181']

        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print(ip)
        # from Wings.models import NoIp
        # Pass_IPs = NoIp.objects.get(id=ip)
        if ip not in Pass_IPs:
            return render(request, 'qiuwo.html')
        else:
            return view_func(request)

    def process_exception(self, request, exception):  # 引发错误 才会触发这个方法
        print("md2  process_exception 方法！")
        # return HttpResponse(exception) #返回错误信息
