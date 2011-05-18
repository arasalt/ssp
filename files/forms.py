from django import forms

from files.models import UserFile

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = UserFile
        exclude = ('user')
