from django.shortcuts import render

# Create your views here.
from app01 import models

def article(request,*args,**kwargs):
    #根据条件查询并显示结果
    article_type_list = models.ArticleType.objects.all() #文章分类
    category_list = models.Category.objects.all() #文章类别

    # 查询条件
    condition = {}
    for k,v in kwargs.items():
        kwargs[k] = int(v) #转换成整形在模板文件中根据匹配变换背景颜色
        if v == '0':
            pass
        else:
            condition[k] = v
    res = models.Article.objects.filter(**condition)
    return render(
        request,
        'article.html',
        {
            'res':res,
            'article_type_list':article_type_list,
            'category_list':category_list,
            'arg':kwargs
        }
    )