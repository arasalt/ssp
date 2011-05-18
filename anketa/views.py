from anketa.models import *
from anketa.forms import *
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

def anketa(request):
    if request.method=="POST":
        
        af=AnketaForm(request.POST,request.FILES)
        print "course:"
        if af.is_valid():
            #af.rezume=request
            af.save()
            return HttpResponseRedirect(reverse('message'))
    else:
        af=AnketaForm()
    rc=RequestContext(request,{'anketaform':af}) 
    return render_to_response("anketa/anketa.html",rc)   

def message(request):
    rc=RequestContext(request)
    return render_to_response("anketa/message.html",rc)


def cv(request):
    if request.method=="POST":
        cvf=CvForm(request.POST,request.FILES)
        if cvf.is_valid():
            #direct=cvf.cleaned_data.get('cv')
           # anketa=Anketa.objects.get()        
            cvf.save()
            rc=RequestContext(request,{'message':'tvoya anketa prinita :)'})
            return render_to_response('message.html',rc)
    else:
        cv=CvForm()
    rc=RequestContext(request,{'cv':cv})
    return render_to_response("anketa/cv.html",rc)