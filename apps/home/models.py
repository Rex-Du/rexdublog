from datetime import datetime

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# tag(标签)
class Tag(models.Model):
    name = models.CharField('标签名称', max_length=30)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 分类
class Category(models.Model):
    name = models.CharField('分类名称', max_length=30)
    index = models.IntegerField('分类的排序', default=999)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    user = models.CharField('作者', max_length=20, default='RexDu')
    image = models.ImageField('图片', upload_to='article/%Y/%m', max_length=100, null=True, blank=True)
    image_url = models.URLField('图片', max_length=400, null=True, blank=True)
    is_banner = models.BooleanField('是否轮播', default=True)
    desc = models.CharField('摘要', max_length=1000)
    detail = RichTextUploadingField('详细内容')
    # category = models.CharField('类别', choices=ARTICLE_CATEGORY_CHOICES, max_length=10)
    category = models.ForeignKey(Category, verbose_name='类别', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField('添加时间', default=datetime.now)
    click_nums = models.IntegerField('点击量', default=0)
    praise_nums = models.IntegerField('点赞数', default=0)
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        # ordering = ['-add_time']

    def __str__(self):
        return self.title


class ReadAndPraise(models.Model):
    ip = models.CharField(verbose_name='用户IP', max_length=20)
    article_id = models.IntegerField('数据id', default=0)  # 直接是收藏对象的id，使用时与fav_type字段一起得出结果
    category = models.IntegerField('收藏类型', choices=((1, '文章'), (2, '分享'), (3, '其它')), default=1)
    add_time = models.DateTimeField('添加时间', default=datetime.now)
    read_nums = models.IntegerField('已读次数', default=0)
    is_praise = models.BooleanField('是否点赞', default=False)

    class Meta:
        verbose_name = '用户点赞'
        verbose_name_plural = verbose_name


# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.CharField(verbose_name='用户', max_length=100)
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章', on_delete=models.DO_NOTHING)
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return str(self.id)


class Visitor(models.Model):
    ip = models.CharField('访客IP', max_length=20)
    visit_time = models.DateTimeField('访问时间', default=datetime.now)
    visit_count = models.IntegerField('访问次数', default=0)

    class Meta:
        verbose_name = '访客信息'
        verbose_name_plural = verbose_name