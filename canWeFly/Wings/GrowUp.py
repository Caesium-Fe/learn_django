from django.utils.deprecation import MiddlewareMixin
# from Wings import views


class MiddleWare(MiddlewareMixin):

    # def __init__(self):
    #     super().__init__()

    def process_request(self, request):
        print("Grow up process_request method success!", id(request))

    def process_response(self, request, response):
        print("Grow up process_response method success!", id(request))
        return response

    def process_view(self, reuqest, view_func, view_args, view_kwargs):
        print("md1  process_view 方法！")  # 在视图之前执行 顺序执行
        return view_func(reuqest)

    def process_exception(self, request, exception):  # 引发错误 才会触发这个方法
        print("md1  process_exception 方法！")
        # return HttpResponse(exception) #返回错误信息
