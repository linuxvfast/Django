#django内置信号的使用
from django.shortcuts import HttpResponse

# Create your views here.
from app01 import models

def signal(request):
    obj = models.User(user='root')
    print('end')
    obj.save()

    obj = models.User(user='test')
    obj.save()

    obj = models.User(user='sysadmin')
    obj.save()
    
    pizza_done.send(sender='seven', toppings=123, size=456) #触发自定义信号
    return HttpResponse('测试')

#访问signal会发现,执行obj = models.User(user='root')之后会调用sg.py中的pre_init方法


#自定义信号

#定义信号
import django.dispatch
pizza_done = django.dispatch.Signal(providing_args=['toppings','size'])

#注册信号
def callback(sender,**kwargs):
    print('callback')
    print(sender,kwargs)

pizza_done.connect(callback)



