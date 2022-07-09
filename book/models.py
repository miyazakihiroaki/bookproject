from sre_constants import CATEGORY
from tabnanny import verbose
from turtle import title
from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]
CATEGORY = (('business', 'ビジネス'),('life', '生活'),('other','その他'))


# modelsモジュールのModelクラスを継承させる
class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    price = models.IntegerField(null=True, blank=True, default=1)
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
        )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # on_delete=models.CASCADEを指定すると、ユーザーが消去された時本全体のデータが消える
    
    # 管理画面でデータの判別をしやすくする
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title