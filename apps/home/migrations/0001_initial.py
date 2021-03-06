# Generated by Django 2.2.4 on 2019-08-31 23:29

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='article/%Y/%m', verbose_name='图片')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否轮播')),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='课程简介')),
                ('detail', models.TextField(verbose_name='详细内容')),
                ('category', models.CharField(choices=[('p', 'Python'), ('l', 'Linux'), ('o', 'Other')], max_length=1, verbose_name='类别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='图片')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]
