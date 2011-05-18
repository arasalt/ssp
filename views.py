from django.shortcuts import render_to_response
from django.template import RequestContext
from discussion.models import *
from discussion.forms import *
from reg.forms import *
def main_page(request):
	rc =RequestContext(request)
	return render_to_response("index.html",rc)
def about_page(request):
	rc =RequestContext(request)
	return render_to_response("about.html",rc)
def graduated(request):
	rc =RequestContext(request)
	return render_to_response("prev_members.html",rc)