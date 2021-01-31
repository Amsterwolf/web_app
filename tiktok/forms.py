from django import forms
from .models import Topic,Entry

class TopicForm (forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text']
        labels={"text":''}#字段text无标签

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text':'excepting your god reply'}
        widgets={'text':forms.Textarea(attrs={'cols':80})}#设置文本区域的为80列

