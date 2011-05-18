from django import forms
from event.models import *
from event.forms import *

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        exclude=('author')
class EventCommentForm(forms.ModelForm):
    class Meta:
        model=CommentEvent
        exclude=('event','author')
        