from django.shortcuts import render

# Create your views here.
from django import forms
from django.shortcuts import redirect
from django.forms import widgets
from django.forms import fields
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError

def mobile_re(value):
    mobile = re.compile(r'^(13[0-9]|15[0-9]|17[678]|18[0-9]|14[57])[0-9]{8}]$')
    if not mobile.match(value):
        raise ValidationError('手机号格式错误')

class FM(forms.Form):
    #字段名和fm文件的名字必须一致
    #字段本身只做验证
    user = fields.CharField(
        error_messages={'required':'用户名不能为空'},
        label='用户名',
        widget=widgets.TextInput(attrs={'class':'c1'}), #自定义属性
        # validators = [RegexValidator(r'^[a-z]+$','请输入数字'),RegexValidator(r'^r[a-z]+$','字母必须以r开头')]
    )
    pwd = fields.CharField(
        max_length=15,
        min_length=6,
        label='密码',
        error_messages={'required':'密码不能为空','min_length':'密码长度不能小于6','max_length':'密码长度不能大于15'},
        widget=widgets.PasswordInput(attrs={'class':'c2'})
    )
    email = fields.EmailField(
        label='邮箱地址',
        error_messages={'required':'邮箱地址不能为空','invalid':'邮箱格式错误'}
    )

    #upload file
    # file = fields.FileField(allow_empty_file=True)

    #radio value
    # city = fields.CharField(
    #     widget=widgets.RadioSelect(choices=((1,'北京'),(2,'上海')))
    # )
    # city2 = fields.ChoiceField(
    #     choices=((1,'北京'),(2,'上海')),
    #     widget=widgets.RadioSelect
    # )
    city = fields.CharField(
        widget=widgets.Select(choices=((1,'北京'),(2,'上海')))
    )
    # city2 = fields.ChoiceField(
    #     choices=((1,'北京'),(2,'上海')),
    #     widget=widgets.Select
    # )

    #more select
    # city = fields.MultipleChoiceField(
    #     choices=((1,'北京'),(2,'上海')),
    #     widget=widgets.SelectMultiple
    # )

    #checkbox multi-select
    # city = fields.MultipleChoiceField(
    #     widget=widgets.CheckboxSelectMultiple,
    #     choices=((1,'北京'),(2,'上海'))
    # )
    phone = fields.CharField(
        validators=[mobile_re,],
        error_messages={'required':'手机号不能为空'},
        widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'手机号'})
    )



def fm(request):
    if request.method == 'GET':
        dic = {
            'user':'root',
            'email':'test@qq.com',
            'city':2
        }
        obj = FM(dic)
        return render(request,'fm.html',{'obj':obj})
    elif request.method == 'POST':
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息
        obj = FM(request.POST)
        is_res = obj.is_valid() #获取结果
        if is_res:
            print(obj.cleaned_data) #获取正确的信息
        else:
            print(obj.errors.as_json()) #可以查看错误的类型【required表示空|invalid表示格式不对】
            # print(obj.errors['user'][0]) #获取错误信息
            # print(obj.errors)
            return render(request,'fm.html',{'obj':obj})
        return redirect('/fm')
