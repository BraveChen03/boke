from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^sendMsg',sendMsg,name='sendMsg'),
    url(r'^getMsg',getMsg,name='getMsg'),

]

