# -*- coding:utf-8 -*-
# my_to_doapp > urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)
]