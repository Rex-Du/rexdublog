from django.urls import path

from .views import ShareView

urlpatterns = [
                    path('', ShareView.as_view(), name='share'),
                                ]
