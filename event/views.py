from event.models import *
from event.forms import *

from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required
def events_list(request):
    events=Event.objects.all()
    rc=RequestContext(request,{'events':events})
    return render_to_response("events/events_list.html",rc)
@login_required
def event_detail(request,event_id):
    event=Event.objects.get(id=event_id)
    com= CommentEvent(event=event,author=request.user)
    print com
    if request.method=="POST":
        ce= EventCommentForm(request.POST,instance=com)
        if ce.is_valid():
            ce.save()
            return HttpResponseRedirect(reverse('event_detail',args=(event_id,)))
    else:
        ce= EventCommentForm(instance=com)
        print ce
    rc=RequestContext(request,{'cform':ce,'event':event})
    return render_to_response("events/event_detail.html",rc)
@login_required
def event_create(request):
    event=Event(author=request.user)
    if request.method=="POST":
        eform=EventForm(request.POST,instance=event)    
        if eform.is_valid():
            eform.save()
            return HttpResponseRedirect(reverse('event_detail',args=(event.id,)))
    else:
        eform=EventForm(instance=event)
    rc=RequestContext(request,{'eform':eform})
    return render_to_response("events/event_create.html",rc)
         
