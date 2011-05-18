from anketa.models import *
from anketa.forms import *
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


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

@login_required
def anketa_list(request):
    anketas=Anketa.objects.all()
    rc =RequestContext(request,{'anketas':anketas})
    return render_to_response("anketa/anketa_list.html",rc)

@login_required
def anketa_detail(request,anketa_id):
    anketa=Anketa.objects.get(id=anketa_id)
    af=WithoutRezume(instance=anketa)
    rc=RequestContext(request,{'af':af,'anketa':anketa})
    return render_to_response("anketa/anketa_detail.html",rc)

@login_required
def invite(request,anketa_id):
    anketa=Anketa.objects.get(id=anketa_id)
    send_mail('Invite','Pozdravliaem','admin@gmail.com',['anketa@mail.mu'],fail_silently=False)
    return render_to_response("anketa/message.html")


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