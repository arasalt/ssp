from django.db import models
from django.forms import ModelForm
from django import forms

class Anketa(models.Model):
	TITLE_CHOICES = (
	    (1, 'first'),
	    (2, 'second'),
	    (3, 'third'),
	    (4, 'fourth'),
)
	name=models.CharField(max_length=30)
        surname=models.CharField(max_length=30)
    	course = models.DecimalField(max_digits=2,decimal_places=1,choices=TITLE_CHOICES)
    	mail=models.EmailField()
    	rezume=models.FileField(upload_to='userdata/anketa/')
    	date=models.DateField(auto_now_add=True)
    	def __unicode__(self):
        	return self.name
    
