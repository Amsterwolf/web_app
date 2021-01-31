from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(req):
    '''注册'''
    if req.method!='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=req.POST)
        if form.is_valid():
            new_user=form.save()
            login(req,new_user)
            return redirect('tiktok:index')
    
    #非提交或非法提交
    context={'form':form}
    return render(req,'registration/register.html',context)