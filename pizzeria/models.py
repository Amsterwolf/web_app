from django.db import models

# Create your models here.
class Pizza(models.Model):
    '''点一份披萨'''
    
    name=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
class Topping(models.Model):
    
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name=models.CharField(max_length=20000)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.name)>20:
            return f"{self.name[:20]}..."
        else:
            return self.name
class Comment(models.Model):
    pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
    comment=models.CharField(max_length=20000)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.comment)>20:
            return self.comment[:20]+'...'
        else:
            return self.comment
