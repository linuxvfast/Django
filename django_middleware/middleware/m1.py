from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

#如果类有process_request,process_view,process_response函数时，会先执行process_request,
# 再执行process_view函数，到达终点之后会反序执行process_response函数
class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('路径1')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('路径4')
    #
    def process_response(self,request,response):
        print('返回1')
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print('路径2')
        # return HttpResponse('检查失败，直接返回异常')
        #如果没有异常，会先从上到下执行process_request函数，在从下到上执行process_response函数
        #如果有异常，会执行process_request函数到异常时停止，然后从异常处向上执行process_response函数


    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('路径5')

    def process_response(self,request,response):
        print('返回2')
        return response

    def process_exception(self, request, exception):
        #添加此方法时，如果执行完process_request和process_view方法,会从下往上找当前方法
        #可对异常进行处理，不处理直接报错
        #处理完异常之后再执行process_response
        if isinstance(exception,ValueError):
            return HttpResponse('异常,程序被中断')

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print('路径3')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('路径6')

    def process_response(self,request,response):
        print('返回3')
        return response

    def process_template_response(self, request, response):
        #如果views中的函数返回的对象中，具有render方法时生效
        print('测试执行')
        return response
