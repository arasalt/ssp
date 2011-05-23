from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
import sha
import random
import re
SHA1_RE = re.compile('^[a-z0-9A-Z]{30}$')
storage = default_storage

class ClientManager(models.Manager):
    def create(self,username,name,surname,email,password):
    	new_user=User.objects.create_user(username,email,password)
    	new_user.is_activate=True
    	new_user.save()
    	client=Client(user=new_user)
        print client
    	client.user_id=new_user.id
    	client.name=name
    	client.surname=surname
        client.activation_key="Activated"
    	client.save()	

class Client(models.Model):
	user=models.ForeignKey(User,unique=True)
	name=models.CharField(max_length=30,blank=True)
	surname=models.CharField(max_length=30,blank=True)
	location=models.CharField(max_length=30,blank=True)
	about=models.CharField(max_length=60,blank=True)
	image = models.ImageField(upload_to="userdata/avatars/", storage=default_storage,blank=True)
	files=models.FileField(upload_to="userdata/files/",blank=True)
	activation_key=models.CharField(('activation_key'),max_length=40,blank=True)
	activated=models.BooleanField(default=False,blank=True)
	create_date = models.DateField(auto_now_add = True,blank=True)
        organizator=models.BooleanField(default=False,blank=True)
        modified_date = models.DateField(auto_now = True,blank=True)
        
	
	objects=ClientManager()

	class Meta:
      	  verbose_name = ('client')
       	  verbose_name_plural = ('clients')
	def __unicode__(self):
		return self.name+" "+self.surname
        @permalink
    	def link_to_self(self):
        	return ('client_profile', (self.id,),)
	@permalink
    	def link_to_edit(self):
        	return ('p_edit', (self.id,),)

	def upload_to_dir(self,filename):
		return 'userdata/files/%s' % (filename)
        
class Entry(models.Model):
    salt=models.CharField(max_length=9)
    registrated=models.BooleanField(default=False)
    def __unicode__(self):
        return self.salt
#	@permalink
#    	def link_to_avatar(self):
 #       return ('account_avatar', (), {})
