from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Event(models.Model):
    author=models.ForeignKey(User)
    title=models.CharField(max_length=50)
    description=models.TextField()
    date=models.DateField()
    start_time=models.TimeField()
    def __unicode__(self):
        return self.title
    
class CommentEvent(models.Model):
    author=models.ForeignKey(User)
    event=models.ForeignKey(Event)
    comment=models.TextField()
    created_date=models.DateField(auto_now_add=True) 
    def __unicode__(self):
        return self.comment   