from django import forms
from reg.models import *
from django.forms.models import *
from django.contrib.auth.models import User

class AvatarForm(forms.Form):
	image=forms.ImageField()

class CvForm(forms.Form):
	cv=forms.FileField()

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('username', 'activation_key', 'activated', 'image','files')

class LoginForm(forms.Form):
	username=forms.CharField(max_length=30)
	password=forms.CharField(max_length = 30, widget = forms.PasswordInput(attrs = {'minlength' : 1}))
	
	#def clean(self):
	#	username=self.cleaned_data.get('username')
	#	password=self.cleaned_data.get('password')
	#if User.objects.all().filter(username=username).count():
	#	raise forms.ValidationError("Your password not correct")
	#else :
	#	raise forms.ValidationError("Your username not correct")	
class RegForm(forms.Form):
	username=forms.CharField(max_length=30)	
	name=forms.CharField(max_length=30)
	surname=forms.CharField(max_length=30)
	mail=forms.EmailField(max_length=30)
	password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'minlength':3}))
	cpassword=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'minlength':3}))

	def clean_username(self):
		username=self.cleaned_data.get('username')
		if User.objects.all().filter(username=username).count():
			raise forms.ValidationError("Username already exist")
		if len(username)<3:
			raise forms.ValidationError("username length must be at least 3")
		return username
	def clean(self):
		pas=self.cleaned_data.get('password')
		cpas=self.cleaned_data.get('cpassword')
		if pas!=cpas:
			raise forms.ValidationError("Password mitmatch")
		if len(pas) < 3:
			raise forms.ValidationError("Password length must be at least 3")
		return self.cleaned_data
	def save(self):
		Client.objects.create(self.cleaned_data['username'],self.cleaned_data['name'],self.cleaned_data['surname'],self.cleaned_data['mail'],self.cleaned_data['password'])
	
        

		
