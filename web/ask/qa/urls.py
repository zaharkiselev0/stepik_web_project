from django.conf.urls import url, include
from django.contrib import admin
from qa.views import test
from qa.q_views import *

urlpatterns = [
 url(r'^$',main,name='main'),
 url(r'^login/$',test,name='test'),
 url(r'^signup/$',test,name='test'),
 url(r'^ask/$',test,name='test'),
 url(r'^new/$',test,name='test'),
 url(r'^popular/$',popular,name='popular'),
 url(r'^question/(?P<id>\d+)/$',question,name='question'),
]
