from django.urls import path
from django.conf.urls import url

from .views import SeriesHomeView

urlpatterns = [
    path('', SeriesHomeView.as_view(), name='series'),
    url(r'series/(?P<series_id>\w+)/$', SeriesHomeView.as_view(), name='series'),
    # url(r'detail/(?P<id>\d+)/$', DetailView.as_view(), name='detail'),
    # url(r'praise/$', PraiseView.as_view(), name='praise'),
    # url(r'comment/(?P<article_id>\d+)$', CommentView.as_view(), name='comment'),
]
