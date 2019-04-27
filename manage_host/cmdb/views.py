from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from cmdb import models
from django.shortcuts import redirect

def add_info(request):
    # models.Host.objects.create(nid=1,hostname='www.a.com',ip='192.168.1.123',port=22,module_id=1)
    # models.Host.objects.create(nid=2,hostname='www.b.com',ip='192.168.1.12',port=3389,module_id=2)
    return HttpResponse('OK')


def business(request):
    v1 = models.Business.objects.all()  #对象
    print(v1)
    v2 = models.Business.objects.all().values('id','caption')   #字典
    v3 = models.Business.objects.all().values_list('id','caption')  #元组
    print(v2)
    print(v3)
    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})

def hosts(request):
    if request.method == 'GET':
        busines_list = models.Business.objects.all()
        v1 = models.Host.objects.filter(nid__gt=0)
        # for row in v1:
        #     print(row.nid,row.hostname,row.ip,row.port,row.module_id,row.module.id,row.module.caption)
        #对象中取值时使用.进行取值
        v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','ip','port','module_id','module__id','module__caption')
        # print(v2)
        # for row in v2:
        #     print(row['nid'],row['hostname'],row['ip'],row['port'],row['module_id'],row['module__id'],row['module__caption'])
        
        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','ip','port','module_id','module__id','module__caption')
        # print(v3)
        # for row in v3:
        #     print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        return render(request,'host.html',{'v1':v1,'v2':v2,'v3':v3,'busines_list':busines_list})
    elif request.method == 'POST':
        host_name = request.POST.get('hostname',None)
        host_ip = request.POST.get('ip',None)
        host_port = request.POST.get('port',None)
        businesid = request.POST.get('module_id',None)
        # print(host_name,host_ip,host_port,businesid)
        models.Host.objects.create(hostname=host_name,ip=host_ip,port=host_port,module_id=businesid)
        return redirect('/cmdb/host')