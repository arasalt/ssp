from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Discussion(models.Model):
	author=models.ForeignKey(User)
	title=models.CharField(max_length=40)
	description=models.TextField()
	create_date=models.DateField(auto_now_add=True)
	modified_date=models.DateField(auto_now=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author=models.ForeignKey(User)
	dis=models.ForeignKey(Discussion)
	comment=models.TextField()
	create_date=models.DateField(auto_now_add=True)
	modified_date=models.DateField(auto_now=True)
	def __unicode__(self):
		return self.comment
