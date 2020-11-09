from django.urls import path
from .views import (TaskListView)
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('staff/', TaskListView.as_view(), name='staff')
]