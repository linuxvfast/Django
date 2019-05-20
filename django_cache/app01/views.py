from django.shortcuts import render

# Create your views here.
import time
from django.views.decorators.cache import cache_page

# @cache_page(10)  #整个页面做缓存
def cache(request):
    current_time = time.time()
    return render(request,'cache.html',{'current_time':current_time})



#如果settings中添加了中间件，views中设置了页面的缓存，模板中设置了局部缓存
#中间件优先级最高，会先通过中间件查看，如果缓存有直接缓存，如果没有查看views中的缓存设置
#如果views中没有，模板中的缓存设置生效