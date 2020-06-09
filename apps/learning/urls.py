from django.urls import path
from django.conf.urls import url

# from .views import LearningView, PythonView, LinuxView, DetailView
from .views import LearningView, DetailView, PraiseView, CommentView

urlpatterns = [
    path('', LearningView.as_view(), name='learning'),
    url(r'category/(?P<category>\w+)/$', LearningView.as_view(), name='category'),
    url(r'detail/(?P<id>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'praise/$', PraiseView.as_view(), name='praise'),
    url(r'comment/(?P<article_id>\d+)$', CommentView.as_view(), name='comment'),
]
