#coding:utf8
from django.shortcuts import render,HttpResponse
#上传 图片模块
from  django.views.decorators.csrf import csrf_exempt #不需要csrf验证
from django.conf import settings
import  json
import  datetime
import  os
import uuid

#上传图片
@csrf_exempt
def upload_image(request,dirname):
    f=request.FILES.get('imgFile',None)
    res = {'error':1,'messqge':'上传失败'}
    if f:
        res = do_upload(f,dirname)
    return HttpResponse(json.dumps(res))
def do_upload(f,dirname):
    file_suffix = f.name.split('.')[-1] #获取文件后缀名
    relative_path=create_dir(dirname)
    name=str(uuid.uuid1())+ '.' + file_suffix #文件名
    fname = os.path.join(settings.MEDIA_ROOT,relative_path,name)
    #把文件写入服务器
    with open(fname,'wb') as file:
        file.write(f.file.read())
    image_url = settings.MEDIA_URL + relative_path + name #图片上传地址
    return {'error':0,'url':image_url}

#创建目录
def create_dir(dirname):
    today = datetime.datetime.today() #获取今天日期
    dirname=dirname + '/%d/%d/' %(today.year,today.month)
    path = os.path.join(settings.MEDIA_ROOT,dirname)
    if not os.path.exists(path):
        os.makedirs(path)
    return dirname
