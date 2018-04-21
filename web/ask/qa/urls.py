from django.conf.urls import url, include
from django.contrib import admin
from qa.views import test
from qa.q_views import *
from qa.ask_views import *
from qa.ans_views import *

urlpatterns = [
 url(r'^ask/$',q_add,name="q_add"),
 url(r'^login/$',test,name='test'),
 url(r'^signup/$',test,name='test'),
 url(r'^new/$',test,name='test'),
 url(r'^popular/$',popular,name='popular'),
 url(r'^question/(?P<id>\d+)/$',question,name='question'),
 url(r'^$',main,name='main'),
]
