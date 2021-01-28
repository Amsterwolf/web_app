from django.shortcuts import render
from .models import Topic
# Create your views here.
def index(req):
    return render(req,'sub_tiktok/indexsite.html')#返回templates文件夹中相应地址的文件

def topics(req):
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(req,'sub_tiktok/topics.html',context)

def topic(req,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')

    context={'topic':topic,'entries':entries}
    return render(req,'sub_tiktok/topic.html',context)