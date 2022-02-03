from django.urls import views
from django.urls.resolvers import URLPattern
from django.urls import path
from . import views


urlpaterns = [
    path('', views.mywow , name="mywow"),
]