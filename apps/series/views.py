from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView

from home.models import Article, Series

# Create your views here.
class SeriesHomeView(APIView):
    def get(self, request, series_id=None):
        if series_id:
            last_series = Series.objects.get(id=series_id)
        else:
            last_series = Series.objects.order_by('-update_time').first()
        series_articels = Article.objects.filter(series=last_series).order_by('add_time')

        each_series_count = Series.objects.annotate(count=Count('article__id')).order_by('-update_time')
        return render(request, 'series.html', locals())
