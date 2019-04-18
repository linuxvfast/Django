# Django

FBV（function base view）
FBV可以说是urls.py规则和view.py函数之间的一种映射关系
在url.py中
			index -> 函数名 #函数名放在view.py中
在view.py中
  我们也可以写成class
		/index/ -> 类 #在url中对应规则为 path('home',views.类名.as_view()),
建议：/index/ -> 类和/index/ -> 函数  两者都用
		
		django是如何识别get和post？？？
			是通过获取General中的
			Request URL: http://localhost:8000/home #通过url中访问的home在url规则中找到对应的类
			Request Method: GET	#在通过get去url规则中对应的类中找get方法
			是基于反射来找方法的，View中的dispatch定义反射查找方法
			请求---》dispatch--》get或post
			也可以自己定义dispatch方法
