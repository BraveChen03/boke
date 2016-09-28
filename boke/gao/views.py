#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout

import  logging #日志器模块
from  django.conf import settings

from  django.db.models import Count
from django.db import connection

from models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage,InvalidPage #分页 3错误提示

from gao.forms import CmmentForm
# Create your views here.
#全局函数
log=logging.getLogger('gao.views')
#全局
def glb_settings(request):

    SITE_URL =settings.SITE_URL
    SITE_NAME =settings.SITE_NAME
    SITE_DESC =settings.SITE_DESC
    MEDIA_URL =settings.MEDIA_URL
    #获取分类
    cats = Category.objects.all()
    tags = Tag.objects.all()
    link = Links.objects.all()
    dids = Ad.objects.all()[:3]
    #浏览量
    article_article = Article.objects.all().order_by('-click_count')[:4]
    # article_click = Article.objects.values('click_count').order_by('-click_count')
    # article_article = article_click.values('title')[:3]
    #站点推荐
    article_recommend= Article.objects.filter(is_recommend=True)

    #评论排行
    comments = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    comment_article = [Article.objects.get( id=comment['article']) for comment in comments]

    #获取归档信息
    # archive = Article.objects.values('date_publish').distinct()
    #执行原生sql 语句
    # cur = connection.cursor()
    # sql = ' SELECT DISTINCT DATE_FORMAT(`gao_article`.`date_publish`,"%Y-%m") FROM `gao_article` LIMIT 21;'
    # archive = cur.execute(sql)
    # res = cur.fetchall()
    # print res
    #扩展objects
    archive = Article.objects.disMon()
    return locals()
#分页显示
def getPage(req,articles):
    pn = req.GET.get('pn',None)
    pagintor = Paginator(articles,2) #第二个参数控制每页记录条数
    try:
        articles = pagintor.page(pn)  #第几页记录
    except(PageNotAnInteger,EmptyPage,InvalidPage),e:
        articles = pagintor.page(1)
    return  articles

def index(req):
    try:
        articles = Article.objects.all()
        articles = getPage(req,articles)
    except Exception,e:
        log.error(e)
    return render(req, 'yin/index.html', locals())

def category(req):
    try:
        cid = req.GET.get('cid',None)
        articles = Article.objects.filter(category=cid)
        articles = getPage(req,articles)
    except Exception,e:
        log.error(e)
    return render(req,'yin/index.html',locals())

def archive(req):
    try:
        y = req.GET.get('y',None)
        m = req.GET.get('m',None)

        if y and m:
            articles = Article.objects.filter(date_publish__icontains=y + '-' + m)
            articles = getPage(req,articles)
    except Exception,e:
        log.error(e)
    return render(req,'yin/index.html',locals())

def tag (req):
    try:
        id = req.GET.get('id',None)
        articles = Article.objects.filter(tag=id)
        articles = getPage(req,articles)
    except Exception,e:
        log.error(e)
    return render(req,'yin/index.html',locals())
# @login_required(login_url='login')
def article(req):
    try:
        aid = req.GET.get('aid',None)
        article = Article.objects.get(id=aid)
        article.click_count = int(article.click_count) +1
        article.save()

        #创建评论表单
        comment_form = CmmentForm({'author' : req.user.username,'aid':aid})

        #获取评论内容
        comments = article.comment_set.all().order_by('id')
        comment_list = []
        for comment in comments:
            #添加子级评论
            for item in comment_list:
                if not hasattr(item,'chrild'):
                    item.chrild = []
                if comment.pid == item:   #item的一条子评论
                    item.chrild.append(comment)
                    break
            if comment.pid is None: #添加父级评论
                comment_list.append(comment)
    except Exception,e:
        log.error(e)
    return render(req, 'yin/article.html', locals())

def comment_post(req):
    comment_form = CmmentForm(req.POST)
    if comment_form.is_valid():
        # 添加数据库
       author = comment_form.cleaned_data['author']
       comment = comment_form.cleaned_data['comment']

       aid = comment_form.cleaned_data['aid']
       Comment.objects.create(content=comment,user=req.user,article_id=aid)
    else:
        return  HttpResponse(comment_form.errors)
    return HttpResponseRedirect(req.META['HTTP_REFERER'])
# return HttpResponseRedirect('/article?aid=%s' % aid)


# def login_x(req):
#     username = req.GET.get('username')
#     password = req.GET.get('password')
#     user = authenticate(username=username,password=password)
#     if user is not None:
#         login(req,user)
#         return HttpResponseRedirect('/')
#     return render(req,'yin/login.html',locals())
def login_x(req):
    if req.method == 'GET': # 请求登陆页面 但没有提交信息
        return render(req,'yin/login.html')
    else:
        print req.POST
        username = req.POST.get('username') #获取用户名

        password = req.POST.get('password') #获取密码
        user = authenticate(username=username,password=password) #
        if user is not None: # 用户存在
            login(req,user) # 执行登陆
            return HttpResponseRedirect('/')
        else:
            return render(req,'yin/login.html',{'log_err':"用户名或密码错误"})

def logout_x(req):
    logout(req)
    return HttpResponseRedirect(req.META['HTTP_REFERER'])






