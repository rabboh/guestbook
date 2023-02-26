#from django.conf.urls import url
from django.urls import path, include
from .views import (
    EntryApiView,
)

urlpatterns = [
    path('', EntryApiView.as_view()),
]