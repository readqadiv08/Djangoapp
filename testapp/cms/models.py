from django.db import models

# Create your models here.
class User(models.Model):
    """ユーザー"""
    name = models.CharField('名前',max_length=255)
    sex = models.CharField('性別',max_length=255)
    age = models.IntegerField('年齢',blank=True)
    
    
    def __str__(self):
        return self.name
    