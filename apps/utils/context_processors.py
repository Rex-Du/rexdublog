# from django.conf import settings  # import the settings file
from django.db.models import Count

from home.models import Category, Article


def categories(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    # return {'CATEGORIES': settings.ARTICLE_CATEGORIES}
    return {'CATEGORIES': Category.objects.order_by('index').values_list('name', flat=True)}


def category_articles(request):
    category_count = Article.objects.values('category_id').annotate(count=Count('category_id')).values('category__name', 'count')
    return {'category_articles': category_count}
