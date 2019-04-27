from django.db import models

# Create your models here.

class Host(models.Model):
    '''host info'''
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4',db_index=True)
    port = models.IntegerField()
    module = models.ForeignKey('Business',to_field='id',on_delete=None)

class Business(models.Model):
    '''business module'''
    caption = models.CharField(max_length=32)