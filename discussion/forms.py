from django import forms
from discussion.models import *
from django.forms.models import *

class DisForm(forms.ModelForm):
	class Meta:
		model=Discussion
		exclude=('create_date','modified_date','author',)
class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		exclude=('author','dis','modified_date',)
	
