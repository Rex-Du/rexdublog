# Generated by Django 2.2.4 on 2019-09-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190910_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=1000, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_banner',
            field=models.BooleanField(default=True, verbose_name='是否轮播'),
        ),
    ]