# Generated by Django 2.2.4 on 2019-09-01 11:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='详细内容'),
        ),
    ]