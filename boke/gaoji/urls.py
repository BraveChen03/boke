#coding:utf8
"""gaoji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from gao import url as gao_url
from  django.views.static import serve
from  django.conf import settings
from  gao.views import *
from gao.upload import upload_image
from qq import urls as qq_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/(.*)$', serve,{'document_root':settings.MEDIA_ROOT}), #指定图片上传路径
    url(r'^admin/upload/(?P<dirname>.+)$',upload_image), #上传图片
    url(r'^', include(gao_url)),
    url(r'^qq', include(qq_urls)),

]

