from django.db import models

# Create your models here.
#customize the third table

class Category(models.Model):
    #类别
    caption = models.CharField(max_length=16)

class ArticleType(models.Model):
    #分类
    caption = models.CharField(max_length=16)

class Article(models.Model):
    #文章
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    article_type = models.ForeignKey(ArticleType,on_delete=models.CASCADE)

    # type_choice = (
    #     (1,'Python'),
    #     (2,'OpenStack'),
    #     (3,'Linux'),
    # )
    # article_type_id = models.IntegerField(choices=type_choice)

