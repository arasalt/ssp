from reg.forms import *
from reg.models import *
from django.shortcuts import *
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.base import ContentFile
from cStringIO import StringIO
import Image 
from django.contrib.auth.decorators import login_required
#import File

def login(request):
	if request.method == "POST":
		lf = LoginForm(request.POST)
		if lf.is_valid():
			user = authenticate(username = lf.cleaned_data.get('username'),password = lf.cleaned_data.get('password'))
			print user
			if user:
				do_login(request, user)
				client=Client.objects.get(user=user)
				rc = RequestContext(request,{'client':client})
				return HttpResponseRedirect(reverse('home_profile'))
	else:
		lf = LoginForm()
	rc = RequestContext(request, {'form' : lf})
	
	return render_to_response('index.html',rc)
@login_required
def logout(request):
	do_logout(request)
	return redirect('main_page')

def register(request):
    if request.method == "POST":
        rf= RegForm(request.POST)
        if rf.is_valid():
            rf.save()
            rc = RequestContext(request, {'message' : 'You must validate your registration. Instruction was sent to you email.'})
            return render_to_response('reg/message.html', rc)
    else:
        rf = RegForm()
    rc = RequestContext(request, {'form' : rf})
    return render_to_response('reg/reg.html', rc)

@login_required
def avatar(request):
	if request.method=="POST":
		avatar=AvatarForm(request.POST,request.FILES)
		
		if avatar.is_valid(): 
			image=avatar.cleaned_data.get('image') 
			
			thumb=Image.open(ContentFile(image.read()))
			thumb.thumbnail((70,80), Image.ANTIALIAS)
			thumb.convert("RGB")
			f = StringIO()
			thumb.save(f, "JPEG")
            		f.seek(0)
			client = Client.objects.get(user = request.user)
            		client.image.save("%s.jpg" % request.user.username, ContentFile(f.read()))
            		return HttpResponseRedirect(reverse('client_profile', args=(request.user.id,)))
	else:	
		avatar=AvatarForm()
	rc=RequestContext(request,{'avatar':avatar})
	return render_to_response("avatar.html",rc)
@login_required
def cv(request):
	if request.method=="POST":
		cvf=CvForm(request.POST,request.FILES)
		if cvf.is_valid():
			direct=cvf.cleaned_data.get('cv')
			#thumb=File.open(ContentFile(direct.read()))
			#print direct
			#f=StringIO()
			#thumb.save(f)
			#f.seek(0)
			client=Client.objects.get(username=request.user)		
			client.files.save("%s" % request.user.username,direct)
			return HttpResponseRedirect(reverse('p_edit',args=(request.user.id,)))	
	else:
		cv=CvForm()
	rc=RequestContext(request,{'cv':cv})
	return render_to_response("cv.html",rc)
@login_required		
def client_profile(request,u_id):
	client=Client.objects.get(pk = u_id)
	rc=RequestContext(request,{'client':client})
	return render_to_response("client_profile.html",rc)
@login_required
def withoutedit(request,user_id):
	client=Client.objects.get(pk = user_id)
	rc=RequestContext(request,{'client':client})
	return render_to_response("withoutedit.html",rc)
@login_required
def profile_edit(request,user_id):
	client=Client.objects.get(pk=user_id)
	if request.method=="POST":
		pf=ClientForm(request.POST,instance=client)
		if pf.is_valid():
			pf.save()
			return HttpResponseRedirect(reverse('client_profile',args=(user.id,)))

	else:
		pf=ClientForm(instance=client)
	rc=RequestContext(request,{"form":pf,"client":client})
	return render_to_response("profile_edit.html",rc)
@login_required
def members(request):
	members=Client.objects.all()
	
	rc=RequestContext(request,{'members':members})
	return render_to_response("members.html",rc)
	
