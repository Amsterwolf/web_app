from django.db import models

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    '''用户添加的内容'''
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.CharField(max_length=200000)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'
    
    def __str__(self):
        if len(self.text)>10:
            return f"{self.text[:10]}..."
        else:
            return self.text