from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def filter_all(arg,key):
    '''
    需要实现的功能
    <!--根据匹配结果变换背景颜色-->
    {% if arg.article_type_id == 0 %}
        <a class="active" class="active" href="/article-0-{{ arg.category_id }}.html">全部</a>
    {% else %}
        <a  href="/article-0-{{ arg.category_id }}.html">全部</a>
    {% endif %}
    {% if arg.category_id == 0 %}
        <a class="active" href="/article-{{ arg.article_type_id }}-0.html">全部</a>
    {% else %}
        <a href="/article-{{ arg.article_type_id }}-0.html">全部</a>
    {% endif %}
    :return:
    '''
    if key == 'article_type_id':
        if arg[key] == 0:
            ret = '<a class="active" href="/article-0-%s.html">全部</a>'%(arg['category_id'])
        else:
            ret = '<a href="/article-0-%s.html">全部</a>'%(arg['category_id'])
    elif key == 'category_id':
        if arg[key] == 0:
            ret = '<a class="active" href="/article-%s-0.html">全部</a>'%(arg['article_type_id'])
        else:
            ret = '<a href="/article-%s-0.html">全部</a>'%(arg['article_type_id'])
    return mark_safe(ret)

@register.simple_tag
def filter_type_list(arg,article_type_list):
    '''
    {% for i in article_type_list %}
        {% if i.id == arg.article_type_id %}
            <a class="active" href="/article-{{ i.id }}-{{ arg.category_id }}.html">{{ i.caption }}</a>
        {% else %}
            <a href="/article-{{ i.id }}-{{ arg.category_id }}.html">{{ i.caption }}</a>
        {% endif %}
    {% endfor %}
    :param arg:
    :return:
    '''
    ret = []
    for row in article_type_list:
        if row.id == arg['article_type_id']:
            temp = '<a class="active" href="/article-%s-%s.html">%s</a>'%(row.id,arg['category_id'],row.caption)
        else:
            temp = '<a href="/article-%s-%s.html">%s</a>'%(row.id,arg['category_id'],row.caption)
        ret.append(temp)
    return mark_safe(''.join(ret))

@register.simple_tag
def filter_cate_list(arg,category_list):
    '''
    实现的功能
    {% for j in category_list %}
        {% if j.id == arg.category_id %}
            <a class="active" href="/article-{{ arg.article_type_id }}-{{ j.id }}.html">{{ j.caption }}</a>
        {% else %}
            <a href="/article-{{ arg.article_type_id }}-{{ j.id }}.html">{{ j.caption }}</a>
        {% endif %}
    {% endfor %}
    :param arg:
    :param category_list:
    :return:
    '''
    ret = []
    for item in category_list:
        if item.id == arg['category_id']:
            temp = '<a class="active" href="/article-%s-%s.html">%s</a>'%(arg['article_type_id'],item.id,item.caption)
        else:
            temp = '<a href="/article-%s-%s.html">%s</a>'%(arg['article_type_id'],item.id,item.caption)
        ret.append(temp)
    return mark_safe(''.join(ret))