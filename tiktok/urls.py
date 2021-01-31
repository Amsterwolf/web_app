'''定义tiktok的url模式'''

from django.urls import path
from . import views

app_name='tiktok'
urlpatterns=[
    
    path('',views.index,name='index'),#主页
    path('topics/',views.topics,name='topics'),#显示所有主题
    path('topics/<int:topic_id>/',views.topic,name='topic'),#显示单个主题
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),



]