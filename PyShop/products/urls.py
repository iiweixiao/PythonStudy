from django.urls import path
from . import views  # 从当前模块引入views

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]