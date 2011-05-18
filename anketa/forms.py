from django import forms
from anketa.models import *
from django.forms.models import *

class AnketaForm(forms.ModelForm):
    class Meta():
        model=Anketa
        exclude=('date')
        
class WithoutRezume(forms.ModelForm):
    class Meta():
        model=Anketa
        exclude=('date','rezume')        
        
