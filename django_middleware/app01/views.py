from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

class Fun:
    def render(self):
        return HttpResponse('OK')

def middle(request):
    # int('dfjaldfjald') #测试异常方法process_exception
    print('最终的目的地---终点')
    # return HttpResponse('中间件')
    return Fun()  #测试方法process_template_response