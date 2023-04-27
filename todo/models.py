from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def one_week():
    return timezone.now().date() + timezone.timedelta(days=7)

class TodoL(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task_name = models.CharField(max_length=200)
    description = models.TextField(max_length=500,null=True,blank=True)
    due_date = models.DateField(default=one_week)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.task_name
    
    
