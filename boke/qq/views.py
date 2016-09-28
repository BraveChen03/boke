#coding:utf8
from django.shortcuts import render,HttpResponse
import json
import datetime
import commen
from models import *
# Create your views here.
#队列字典
whole_dict = {} #全局用户字典
def index(req):
    groups = QQGroup.objects.filter(members=req.user).all()
    return render(req,'qq/index.html',locals())

def sendMsg(req):
    data = req.POST.get('data',None)
    data = json.loads(data) #转换json 成为 字典
    data['time'] = datetime.datetime.now().strftime('%Y%m%d %H:%I:%S')
    to_id = int(data['to_id'])
    contact_type = data['contact_type']
    if contact_type == 'single':
        if to_id not in whole_dict: #消息不在队列创建
            whole_dict[to_id] = commen.Player()
        try:
            whole_dict[to_id].msg_q.put(data)
            return HttpResponse('ok')
        except Exception,e:
            print e
            return HttpResponse('发送失败')
    elif contact_type == 'group':
        group_id = data['to_id']
        group = QQGroup.objects.get(id=group_id)
        data['from_id'] = group_id

        #循环组内所有成员，想每个成员消息队列添加一条消息
        for user in group.members.all():
            if user.id not in whole_dict: #消息不在队列创建
                whole_dict[user.id] = commen.Player()
            try:
                if user.id !=req.user.id:
                    whole_dict[user.id].msg_q.put(data)

            except Exception,e:
                print e
                return HttpResponse('发送失败')
        return HttpResponse('ok')

def getMsg(req):
    uid =req.GET.get('uid',None)
    if uid is not None:
        uid = int(uid)
        if uid not in whole_dict:
            whole_dict[uid] = commen.Player()
        try:
            msgs = whole_dict[uid].getMsg()
            return HttpResponse(json.dumps(msgs))
        except Exception,e:
            print e
    else:
        return HttpResponse('get message error')



