使用组件搜索的两种方式
1、组合搜索组件（自定义第三张表）

2、
如何需要自动创建第三张表需要把上面model.py文件中的第三张表删除，使用自定义的type_choice字段
views.py中使用article_type_list = models.Article.type_choice获取结果
自定义sample_tag中遍历第三张表时用元组的获取方式row[0]获取第一个结果
