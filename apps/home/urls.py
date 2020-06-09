from django.contrib import admin
from django.urls import path

from .views import HomePageView, LoginView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('login/', LoginView.as_view(), name='login')
]
