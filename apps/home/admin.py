from django.contrib import admin
from .models import Article, ReadAndPraise, Tag, Category, Visitor, Series


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_banner', 'category', 'add_time', 'click_nums', '标签')

    def 标签(self, article):
        return [tag.name for tag in article.tags.all()]


class ReadAndFavoriteAdmin(admin.ModelAdmin):
    list_display = ('ip', 'article_id', 'category', 'read_nums', 'is_praise')


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'visit_time', 'visit_count')


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ReadAndPraise, ReadAndFavoriteAdmin)
admin.site.register(Tag)
admin.site.register(Series)
admin.site.register(Category)
admin.site.register(Visitor, VisitorAdmin)
