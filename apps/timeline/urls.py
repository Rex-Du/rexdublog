from django.urls import path

from .views import TimeLineView

urlpatterns = [
    path('', TimeLineView.as_view(), name='timeline'),
]
