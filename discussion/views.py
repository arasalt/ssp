# Create your views here.
from discussion.models import *
from discussion.forms import *
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required
def home_profile(request):
	author=User.objects.get(username=request.user)
		
	rc=RequestContext(request,{'author':author})
	return render_to_response("home_profile.html",rc)
@login_required
def create_dis(request):
	dis=Discussion(author=request.user)
	print dis
	if request.method=="POST":
		df=DisForm(request.POST,instance=dis)
		if df.is_valid():
			df.save()
			
			return HttpResponseRedirect(reverse("dis_detail",args=(dis.id,)))
	else:
		df=DisForm(instance=dis)
	rc=RequestContext(request,{'df':df})
	return render_to_response("dis/create_dis.html",rc)
@login_required
def dis_detail(request,dis_id):
	dis=Discussion.objects.get(id=dis_id)
	comment=Comment(dis=dis,author=request.user)
	
	if request.method=="POST":
		cf=CommentForm(request.POST,instance=comment)
		if cf.is_valid():
			cf.save()
			HttpResponseRedirect(reverse("dis_detail",args=(dis_id,)))
	else:
		cf=CommentForm(instance=comment)
	rc=RequestContext(request,{'dis':dis,'cform':cf})
	return render_to_response("dis/dis_detail.html",rc)
@login_required	
def dis_list(request):
	diss=Discussion.objects.all().order_by('create_date')[:10]
	rc=RequestContext(request,{'diss':diss})
	return render_to_response("dis/dis_list.html",rc)
