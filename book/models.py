from sre_constants import CATEGORY
from turtle import title
from django.db import models

CATEGORY = (('business', 'ビジネス'),('life', '生活'),('other','その他'))
# modelsモジュールのModelクラスを継承させる
class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
        )
    
    # 管理画面でデータの判別をしやすくする
    def __str__(self):
        return self.title