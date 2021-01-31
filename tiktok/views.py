from django.shortcuts import render,redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def check_topic_owner(req,topic):
    if topic.owner!=req.user:
        raise Http404
def index(req):
    return render(req,'sub_tiktok/indexsite.html')#返回templates文件夹中相应地址的文件

@login_required#已登录才放行
def topics(req):
    topics=Topic.objects.filter(owner=req.user).order_by('date_added')#过滤出指向该用户的topics
    context={'topics':topics}
    return render(req,'sub_tiktok/topics.html',context)

@login_required
def topic(req,topic_id):
    topic=Topic.objects.get(id=topic_id)
    check_topic_owner(req,topic)
    
    entries=topic.entry_set.order_by('-date_added')

    context={'topic':topic,'entries':entries}
    return render(req,'sub_tiktok/topic.html',context)

@login_required
def new_topic(req):
    if req.method!='POST':
        form=TopicForm()
    else:
        form=TopicForm(data=req.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=req.user
            new_topic.save()
            return redirect("tiktok:topics")
    
    #显示空表或指出表单数据无效
    context={'form':form}
    return render(req,"sub_tiktok/new_topic.html",context)

@login_required
def new_entry(req,topic_id):
    topic=Topic.objects.get(id=topic_id)
    
    check_topic_owner(req,topic)

    if req.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=req.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect("tiktok:topic",topic_id=topic_id)#提交成功后重定向
    
    #显示空表或指出表单数据无效
    context={'form':form,'topic':topic}#显示用
    return render(req,"sub_tiktok/new_entry.html",context)

@login_required
def edit_entry(req,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic

    check_topic_owner(req,topic)

    if req.method!='POST':
        form=EntryForm(instance=entry)#样例填充（非空表单）
    else:
        form=EntryForm(instance=entry,data=req.POST)#继承instance
        if form.is_valid():
            form.save()
            return redirect('tiktok:topic',topic_id=topic.id)
    
    context={'entry':entry,'topic':topic,'form':form}
    return render(req,'sub_tiktok/edit_entry.html',context)

