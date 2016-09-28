#coding:utf8
from  __future__ import unicode_literals
from django.db import models
from  django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    avatar=models.ImageField(upload_to='avatar/%Y/%m',default='upload/default.jpg',max_length=100,verbose_name='头像')
    qq = models.CharField(max_length=15,verbose_name='QQ',blank=True)
    phone = models.CharField('电话',max_length=23,blank=True)
    url = models.URLField('个人主页',max_length=30,blank=True)
    nick = models.CharField('昵称',max_length=30,blank=True)
    friend = models.ManyToManyField('self',verbose_name='朋友',blank=True,null=True)
    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name
        ordering=['id']
    def __unicode__(self):
        return self.username




class Tag(models.Model):
    name=models.CharField(max_length=50,verbose_name='标签字')
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
        ordering=['-id']
    def __unicode__(self):
        return self.name
#月份归档
class ArticleManager(models.Manager):
    def disMon(self):
        res = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y年%m月文章归档'.encode('utf-8'))
            if date not in res:
                res.append(date)
        return res

class Article(models.Model):
    title=models.CharField('标题',max_length=30)
    desc=models.CharField('简介',max_length=100)
    content=models.TextField('内容')
    click_count=models.IntegerField(default=0,verbose_name='点击量')
    is_recommend=models.BooleanField(default=False,verbose_name='是否推荐')
    date_publish=models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    category=models.ForeignKey('Category',verbose_name='文章分类')
    user=models.ForeignKey(User,verbose_name='用户')
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    objects = ArticleManager()
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name=models.CharField('名字',max_length=30)
    index=models.IntegerField(default=999,verbose_name='从小到大排列')
    class Meta:
        verbose_name='文章分类'
        verbose_name_plural=verbose_name
        ordering=['index']
    def __unicode__(self):
        return self.name
class Comment(models.Model):
    content=models.TextField('评论内容')
    date_publish=models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    article=models.ForeignKey(Article,verbose_name='文章')
    pid=models.ForeignKey('self',verbose_name='父级评论',blank=True,null=True)
    user=models.ForeignKey(User,verbose_name='用户',blank=True)
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name
        ordering=['-date_publish','id']
    def __unicode__(self):
        return self.content

class Ad(models.Model):
    title=models.CharField('标题',max_length=30)
    desc=models.TextField('广告简介',max_length=100,blank=True)
    image_url = models.ImageField(upload_to='ad/%Y/%m',default='upload/default.jpg',max_length=100,verbose_name='图片地址')
    callback_url=models.URLField('广告连接',max_length=255,blank=True)
    date_publish = models.DateTimeField('添加时间',auto_now_add=True,)
    index=models.IntegerField('从小到大排序',default=999)
    class Meta:
        verbose_name='广告'
        verbose_name_plural=verbose_name
        ordering=['index','-date_publish']
    def __unicode__(self):
        return self.title

class Links(models.Model):
    title=models.CharField('链接标题',max_length=30)
    desc=models.TextField('链接简介',max_length=100)
    callback_url = models.URLField(max_length=255,verbose_name='链接地址',blank=True)
    date_publish=models.DateTimeField('添加时间',auto_now_add=True,)
    index=models.IntegerField('从小到大排序',default=999)
    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name
        ordering = ['index','-date_publish']
    def __unicode__(self):
        return self.title