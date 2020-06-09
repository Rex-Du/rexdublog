from datetime import datetime

from django.db import models


# Create your models here.
class Experiences(models.Model):
    content = models.CharField('心得', max_length=500)
    image = models.ImageField('图片', upload_to='about/%Y/%m', max_length=100, null=True, blank=True)
    image_url = models.URLField('图片', max_length=400, null=True, blank=True)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '感悟'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
